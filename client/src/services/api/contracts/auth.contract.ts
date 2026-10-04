export interface RegisterRequest {
  username: string;
  email: string;
  password: string;
}

export interface User {
  id: string;
  username: string;
  email: string;
  biography: string | null;
  avatar_url: string | null;
  created_at: string;
}
