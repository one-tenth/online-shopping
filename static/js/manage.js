function changeQuantity(id, delta) {
    const input = document.getElementById(id);
    const currentValue = parseInt(input.value);
    const newValue = currentValue + delta;
    if (newValue >= 0 && newValue <= input.max) {
        input.value = newValue;
        calculateTotal(); // 更新總金額
    }
}