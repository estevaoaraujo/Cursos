//               012345678
let umaString = 'Meu valor';

// length

// Caractere de escape \
console.log(umaString.charAt(-1)); // Retorna o valor da pos
console.log(umaString.charCodeAt(4)); // Retorna o código inteiro que repsetanta o valor na tabela asc
console.log(umaString.concat(' ', 'ei', ' ', 'sister')); // raramente usado
console.log(umaString.indexOf('e', 0)); // Retorna o índice
console.log(umaString.lastIndexOf('e', umaString.length)); // Retorna o índice
console.log(umaString.match(/[A-Za-z]+/g)); // Retorna um array com os valores encontrados (se g)
console.log(umaString.search(/[a-z]+/g)); // Retorna o índice da primeira ocorrência
console.log(umaString.replace(/e/g, '3'));//    Substitui valores
console.log(umaString.slice(2, 7));// Pega parte da string
console.log(umaString.slice(-3, -1));// Conta de trás para frente
console.log(umaString.split(' ', 2));// Retorna um array
console.log(umaString.toUpperCase());// Retorna a string em maiúsculo
console.log(umaString.toLowerCase());    // Retorna a string em minúsculo
console.log(umaString.trim()); // Remove espaços em branco no início e no fim da string
console.log(umaString.includes('val'));// Retorna true ou false
console.log(umaString.startsWith('Meu'));// Retorna true ou false
console.log(umaString.endsWith('or'));// Retorna true ou false
console.log(umaString.repeat(3));// Repete a string n vezes
console.log(umaString.padStart(20, '.'));// Adiciona caracteres no início da string até o tamanho definido
console.log(umaString.padEnd(20, '.'));// Adiciona caracteres no fim da string até o tamanho definido
console.log(umaString.normalize('NFD'));// Normaliza a string
console.log(umaString.normalize('NFC'));// Normaliza a string
console.log(umaString.normalize('NFKD'));// Normaliza a string
console.log(umaString.normalize('NFKC'));// Normaliza a string
console.log(umaString.valueOf());// Retorna o valor primitivo da string
console.log(umaString.toString());// Retorna a string como objeto
console.log(umaString.anchor('meuAnchor'));// Cria uma âncora
console.log(umaString.big());// Retorna a string em uma fonte maior
console.log(umaString.blink());// Retorna a string piscando
console.log(umaString.bold());// Retorna a string em negrito
console.log(umaString.fixed());// Retorna a string em uma fonte de largura fixa
console.log(umaString.fontcolor('red'));// Retorna a string com a cor da fonte definida
console.log(umaString.fontsize(20));// Retorna a string com o tamanho da fonte definido
console.log(umaString.italics());// Retorna a string em itálico
console.log(umaString.link('http://www.example.com'));// Retorna a string como um link
console.log(umaString.small());// Retorna a string em uma fonte menor
console.log(umaString.strike());// Retorna a string com uma linha no meio
console.log(umaString.sub());// Retorna a string como subscrito
console.log(umaString.sup());// Retorna a string como sobrescrito

console.log(umaString);
