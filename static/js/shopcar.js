function changeQuantity(id, delta) {
    const input = document.getElementById(id);
    const currentValue = parseInt(input.value);
    const newValue = currentValue + delta;
    if (newValue >= 0 && newValue <= input.max) {
        input.value = newValue;
        calculateTotal(); // 更新總金額
    }
}

function calculateTotal() {
    const checkboxes = document.querySelectorAll('.product .check');
    let total = 0;

    checkboxes.forEach((checkbox, index) => {
        if (checkbox.checked) {
            const priceElement = document.querySelectorAll('.product .pp')[index];
            const quantityElement = document.querySelectorAll('.product .quantity')[index];
            const price = parseFloat(priceElement.textContent.replace('$', ''));
            const quantity = parseInt(quantityElement.value);
            total += price * quantity;
        }
    });

    const totalElement = document.getElementById('tot-t');
    totalElement.textContent = `總金額$${total.toFixed(0)}`;
}

function toggleAll(source) {
    const checkboxes = document.querySelectorAll('.product .check');
    checkboxes.forEach(checkbox => checkbox.checked = source.checked);
    calculateTotal(); // 更新總金額
}

function checkAllSelected() {
    const checkboxes = document.querySelectorAll('.product .check');
    const allChecked = Array.from(checkboxes).every(checkbox => checkbox.checked);
    document.getElementById('check-all').checked = allChecked;
}

function resetCart() {
    const checkboxes = document.querySelectorAll('.product .check');
    const quantities = document.querySelectorAll('.product .quantity');

    checkboxes.forEach(checkbox => checkbox.checked = false);
    quantities.forEach(quantity => quantity.value = 0);

    document.getElementById('check-all').checked = false; // 取消全選
    calculateTotal(); // 重置後更新總金額
}
