Yes. I'd make the prompt fairly strict so an AI coding assistant understands that **TanStack Query owns server state**, while your existing Redux/Saga patterns should not be introduced for new API work.

# API and Code Structure Guidelines

Follow these guidelines whenever adding or modifying API integrations in this project.

## 1. Core Architecture

Use the following architecture for API-driven features:

```text
Component
    ↓
TanStack Query Hook
    ↓
API Function
    ↓
Axios Client
    ↓
Backend API
```

Do **not** introduce Redux actions, reducers, selectors, or Redux Saga for new API integrations unless explicitly required for a non-server-state use case.

TanStack Query should be the primary solution for:

- Fetching server data
- Caching server data
- Loading states
- Error states
- Refetching
- Query invalidation
- Mutations
- Pagination
- Infinite queries
- Optimistic updates where appropriate

Redux should only be used for genuine client/global application state, not as a duplicate store for API/server data.

---

# 2. Folder Structure

Organize API-related code by entity/feature.

A recommended structure is:

```text
src/
├── api/
│   ├── client/
│   │   └── axios.ts
│   │
│   ├── contracts/
│   │   ├── user.contract.ts
│   │   ├── mine.contract.ts
│   │   └── ...
│   │
│   ├── entities/
│   │   ├── user/
│   │   │   ├── user.api.ts
│   │   │   ├── user.queries.ts
│   │   │   ├── user.mutations.ts
│   │   │   └── index.ts
│   │   │
│   │   ├── mine/
│   │   │   ├── mine.api.ts
│   │   │   ├── mine.queries.ts
│   │   │   ├── mine.mutations.ts
│   │   │   └── index.ts
│   │   │
│   │   └── ...
│   │
│   └── index.ts
│
├── interfaces/
│   ├── api.interface.ts
│   ├── common.interface.ts
│   └── index.ts
│
├── constants/
│   └── api.ts
│
├── components/
├── pages/
└── ...
```

The exact existing project structure should be respected where possible. Do not reorganize unrelated code just to follow this structure.

---

# 3. Entity Contracts

Each API entity should have its request and response contracts defined separately from the API implementation.

For example:

```text
api/
└── contracts/
    └── mine.contract.ts
```

Example:

```ts
export interface Mine {
  id: string;
  name: string;
  location: string;
}

export interface MineListRequest {
  params: {
    page?: number;
    limit?: number;
    search?: string;
  };
}

export interface MineListResponse {
  data: Mine[];
}
```

Keep entity-specific interfaces in the entity's contract file.

Do not place entity-specific interfaces in the global/common interfaces file.

---

# 4. Global API Response Contract

Create a common generic API response interface.

For example:

```ts
export type ApiStatus = 'success' | 'error';

export interface APIResponse<T> {
  status: ApiStatus;
  status_code: string;
  data: T;
}
```

This interface should be reused across all API endpoints.

For example:

```ts
APIResponse<User>
```

or:

```ts
APIResponse<Mine[]>
```

Do not redefine this response structure separately for every entity.

---

# 5. Common Interfaces

Global interfaces should contain only genuinely reusable concepts.

Examples:

```ts
export interface PaginationParams {
  page?: number;
  limit?: number;
}

export interface PaginationMeta {
  page: number;
  limit: number;
  total: number;
  total_pages: number;
}
```

Avoid putting entity-specific interfaces here.

A good rule is:

> If the interface only makes sense for one entity, keep it with that entity.

---

# 6. API Functions

API functions should be thin wrappers around the Axios client.

Example:

```ts
export async function getMinesList(
  params: MineListRequest['params']
) {
  return createAxiosInstance({
    method: 'GET',
    url: API_URL.mines,
    params,
  });
}
```

API functions should:

- Define the endpoint
- Pass request parameters/body
- Use the shared Axios client
- Have proper TypeScript types

API functions should NOT:

- Manage React state
- Call React hooks
- Dispatch Redux actions
- Interact with Redux
- Contain TanStack Query logic

Keep API functions framework-independent.

---

# 7. Axios Client

Use a centralized Axios client for common HTTP behavior.

The Axios client should handle concerns such as:

- Base URL
- Credentials
- Headers
- Query parameter serialization
- Authentication
- Token refresh
- Request cancellation
- Response handling
- Common HTTP errors
- Request/response interceptors
- Encryption/decryption if required

The Axios client should remain independent of React and TanStack Query.

Most importantly:

> HTTP errors must reject the promise.

For example, 4xx and 5xx responses should result in an Axios error being thrown/rejected so TanStack Query can correctly populate its `error` state.

Do not silently convert HTTP errors into successful promise resolutions.

---

# 8. TanStack Query

Use TanStack Query for general API/server-state operations.

For queries, create reusable query hooks.

Example:

```ts
export function useMinesList(
  params: MineListRequest['params']
) {
  return useQuery({
    queryKey: ['mines', params],
    queryFn: () => getMinesList(params),
  });
}
```

Components should consume the query hook:

```ts
const {
  data,
  isLoading,
  isFetching,
  error,
} = useMinesList(params);
```

Do not call Axios directly from components.

Do not create `useEffect` + Axios patterns for normal API fetching.

---

# 9. API Response Wrapper

The project uses a common API response structure:

```json
{
  "status": "success",
  "status_code": "S-10001",
  "data": {}
}
```

Create a reusable wrapper around TanStack Query so consumers can work with:

```ts
{
  data,
  apiStatus,
  statusCode,
  error,
  isLoading,
  isFetching,
  ...
}
```

The important distinction is:

```text
data
→ APIResponse.data

apiStatus
→ APIResponse.status

statusCode
→ APIResponse.status_code

error
→ Axios/TanStack transport or HTTP error
```

Do not confuse the backend `status` with TanStack Query's own query status.

Prefer names such as:

```ts
apiStatus
statusCode
```

instead of exposing two different concepts under `status`.

---

# 10. Error Handling

There are two different types of failure.

### Application-level API error

The backend successfully responds with:

```json
{
  "status": "error",
  "status_code": "E-10001",
  "data": null
}
```

This is still a successful HTTP request.

The wrapper should expose:

```ts
apiStatus: 'error'
statusCode: 'E-10001'
error: null
```

### HTTP/network error

Examples:

- 400
- 401
- 403
- 404
- 422
- 500
- Network failure
- Request timeout

These should reject through Axios and be exposed through TanStack Query's:

```ts
error
```

The application should not duplicate HTTP error information into Redux.

---

# 11. Mutations

Use TanStack Query's `useMutation` for:

- POST
- PUT
- PATCH
- DELETE

Example:

```ts
export function useCreateMine() {
  return useMutation({
    mutationFn: createMine,
    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ['mines'],
      });
    },
  });
}
```

After a mutation, invalidate or update the relevant query cache instead of manually synchronizing Redux state.

---

# 12. Query Keys

Query keys must be predictable and consistent.

Examples:

```ts
['me']

['mines']

['mines', params]

['mine', mineId]
```

Prefer central query-key definitions for complex entities:

```ts
export const mineKeys = {
  all: ['mines'] as const,
  lists: () => [...mineKeys.all, 'list'] as const,
  list: (params: MineListRequest['params']) =>
    [...mineKeys.lists(), params] as const,
  details: () => [...mineKeys.all, 'detail'] as const,
  detail: (id: string) =>
    [...mineKeys.details(), id] as const,
};
```

Use these keys consistently for queries and invalidation.

---

# 13. Type Safety

The API layer must be fully type-safe.

Avoid:

```ts
any
```

unless there is a strong technical reason.

Prefer generics:

```ts
APIResponse<T>
```

and typed API functions:

```ts
async function getMinesList(
  params: MineListRequest['params']
): Promise<APIResponse<Mine[]>> {
  ...
}
```

The expected types should flow through:

```text
API Contract
    ↓
API Function
    ↓
Axios
    ↓
TanStack Query
    ↓
Custom Query Wrapper
    ↓
React Component
```

A component consuming:

```ts
const { data } = useMinesList(params);
```

should automatically know that:

```ts
data
```

is:

```ts
Mine[] | undefined
```

without manually casting it.

---

# 14. Do Not Duplicate Server State

Do not copy TanStack Query data into Redux.

Avoid:

```ts
const { data } = useMinesList();

useEffect(() => {
  dispatch(setMines(data));
}, [data]);
```

TanStack Query should remain the source of truth for server data.

Similarly, do not maintain a separate local state copy of API data unless there is a specific reason, such as an editable draft.

---

# 15. Redux Usage

Redux may still be used for genuine client-side/global state.

Examples include:

- Complex client-only workflows
- Global UI state
- Application preferences
- Temporary client-side state
- State that does not represent cached server data

Do not use Redux/Saga for standard API CRUD operations when TanStack Query can handle them.

---

# 16. New API Development Workflow

When adding a new API:

### Step 1: Define the contract

Create or update the relevant entity contract:

```text
api/contracts/mine.contract.ts
```

### Step 2: Add endpoint constant

```ts
API_URL.mines
```

### Step 3: Add API function

```ts
getMinesList()
createMine()
updateMine()
deleteMine()
```

### Step 4: Add TanStack Query hooks

```ts
useMinesList()
useMine()
useCreateMine()
useUpdateMine()
useDeleteMine()
```

### Step 5: Use the hooks from components

Components should consume the hooks rather than Axios directly.

### Step 6: Handle cache invalidation

After mutations, invalidate or update the relevant query keys.

---

# 17. General Rule

When implementing any new feature, first determine whether the state is:

```text
Server State
    → TanStack Query

Client/UI State
    → Redux or appropriate local state solution

URL State
    → Router/search params

Form State
    → Form state solution
```

Do not automatically use Redux simply because an API is involved.

The preferred default for API/server-state work is:

```text
React
  ↓
TanStack Query
  ↓
API Function
  ↓
Shared Axios Client
  ↓
Backend
```