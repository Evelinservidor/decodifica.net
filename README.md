# Decodifica.net

> IA en español, sin fluff. Noticias, análisis y tutoriales prácticos de inteligencia artificial.

Sitio web oficial del proyecto Decodifica. Construido con [Astro](https://astro.build) + [Supabase](https://supabase.com) + [Tailwind CSS](https://tailwindcss.com).

## Stack

- **Framework**: [Astro 4](https://astro.build) (SSG con islands)
- **Styling**: [Tailwind CSS 3](https://tailwindcss.com)
- **Backend**: [Supabase](https://supabase.com) (Auth, DB, Storage, Realtime)
- **Newsletter**: [Buttondown](https://buttondown.com)
- **Analytics**: [Plausible](https://plausible.io)
- **Hosting**: [GitHub Pages](https://pages.github.com)
- **CI/CD**: GitHub Actions

## Estructura

```
decodifica.net/
├── src/
│   ├── components/        # Componentes reutilizables
│   ├── layouts/           # Layouts base
│   ├── pages/             # Rutas (file-based)
│   │   ├── api/           # Endpoints del backend
│   │   └── blog/          # Páginas dinámicas
│   ├── lib/               # Lógica de negocio
│   │   ├── supabase.ts    # Cliente Supabase
│   │   ├── auth.ts        # Helpers de auth
│   │   └── content.ts     # Helpers de contenido
│   ├── content/           # Blog posts en MD/MDX
│   └── styles/            # CSS global
├── public/                # Assets estáticos
├── .env.example           # Plantilla de variables
├── astro.config.mjs       # Config de Astro
└── tailwind.config.mjs    # Config de Tailwind
```

## Setup local

### Requisitos

- Node.js >= 20
- npm >= 10
- Cuenta en [Supabase](https://supabase.com) (gratis)
- Cuenta en [Buttondown](https://buttondown.com) (gratis)

### Instalación

```bash
# Clonar repo
git clone https://github.com/Evelinservidor/decodifica.net.git
cd decodifica.net

# Instalar dependencias
npm install

# Copiar variables de entorno
cp .env.example .env.local

# Editar .env.local con tus credenciales reales
# (SUPABASE_URL, SUPABASE_ANON_KEY, BUTTONDOWN_USERNAME)

# Arrancar dev server
npm run dev
```

Abre [http://localhost:4321](http://localhost:4321) en tu navegador.

## Scripts

| Script | Descripción |
|--------|-------------|
| `npm run dev` | Servidor de desarrollo |
| `npm run build` | Build para producción |
| `npm run preview` | Preview del build |
| `npm run lint` | Linting con ESLint |
| `npm run format` | Formatear con Prettier |
| `npm run type-check` | TypeScript check |
| `npm run audit` | Auditoría de dependencias |

## Deploy

El deploy es automático con GitHub Actions en cada push a `main`. Ver `.github/workflows/deploy.yml`.

URL de producción: [https://decodifica.net](https://decodifica.net)

## Seguridad

- ✅ TypeScript estricto en todo el código
- ✅ Secrets solo en `.env.local` (gitignored)
- ✅ Variables públicas con prefijo `PUBLIC_`
- ✅ RLS activado en todas las tablas de Supabase
- ✅ CSP headers en producción
- ✅ HTTPS forzado
- ✅ Sanitización de HTML en contenido de usuario

## Licencia

MIT © Jordi / Decodifica
