import prettierPluginAstro from 'prettier-plugin-astro';
export default {
  plugins: [prettierPluginAstro],
  printWidth: 100,
  semi: true,
  singleQuote: true,
  trailingComma: 'es5',
  bracketSpacing: true,
  arrowParens: 'always',
  overrides: [
    {
      files: '*.astro',
      options: { parser: 'astro' },
    },
  ],
};
