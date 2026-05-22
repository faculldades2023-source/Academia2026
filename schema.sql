-- 1. Cria a tabela de usuários e estados
create table public.users (
  id text primary key,
  state jsonb not null,
  updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 2. Habilita a segurança em nível de linha (RLS)
alter table public.users enable row level security;

-- 3. Cria política para permitir leitura e escrita anônima
create policy "Permitir leitura e escrita publica"
on public.users
for all
using (true)
with check (true);

-- 4. Habilita o Realtime (tempo real) para esta tabela
alter publication supabase_realtime add table public.users;
