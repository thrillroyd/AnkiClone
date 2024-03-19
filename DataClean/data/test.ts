import fs from 'fs'


// const vocabs = JSON.parse('deck.json')
const vocabs = JSON.parse(fs.readFileSync('deck.json', 'utf-8'))
console.log(vocabs)