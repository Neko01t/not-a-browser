import jsdom from 'jsdom';
const { JSDOM } = jsdom;


const response = await fetch('https://google.com');
const data = await response.text();
const dom = new JSDOM(data);
console.log(dom.window.document.querySelector("title").textContent);

