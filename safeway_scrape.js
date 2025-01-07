const products_array = Array(...document.querySelectorAll('[class=product-title__text]'));
const products = products_array.map((parent) => parent.textContent.trim());

const price_array = Array(...document.querySelectorAll('[data-qa=prd-itm-prc]'));
const price = price_array.map((parent) => parent.children[0].nextSibling.textContent.trim());

const result = {};
for (let i = 0; i < products.length; i++) {  
    result[products[i]] = price[i]; 
}  

console.log(result);

