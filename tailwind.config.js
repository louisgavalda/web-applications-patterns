/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './_content/*.html',
        './_content/**/*.html',
        './_content/**/*.njk',
        './templates/*.html',
        './agenda/templates/**/*.html',
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}
