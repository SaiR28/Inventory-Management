const cartItems = [];

const addCartItem = (item) => {
  cartItems.push(item);
  updateCart();
}

const updateCart = () => {
  const cartList = document.querySelector('#cart ul');
  cartList.innerHTML = '';

  let total = 0;

  for (const item of cartItems) {
    const cartItem = document.createElement('li');
    cartItem.innerText = `${item.name} - $${item.price.toFixed(2)}`;
    cartList.appendChild(cartItem);

    total += item.price;
  }

  document.querySelector('#total').innerText = total.toFixed(2);
}

document.querySelectorAll('.add-to-cart').forEach(button => {
  button.addEventListener('click', () => {
    const product = button.parentNode;
    const name = product.querySelector('h3').innerText;
    const price = parseFloat(product.querySelector('p:last-of-type').innerText.replace('$', ''));
    addCartItem({ name, price });
  });
});

document.querySelector('#checkout').addEventListener('click', () => {
  alert('Thank you for your purchase!');
  cartItems.length = 0;
  updateCart();
});