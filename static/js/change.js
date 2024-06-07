window.onload = function() {
    const birthYearSelect = document.getElementById('birth-year');
    const startYear = 2006; // 民国95年
    const endYear = 1954; // 民国43年

    for (let year = startYear; year >= endYear; year--) {
        const option = document.createElement('option');
        option.value = year;
        option.text = year;
        birthYearSelect.add(option);
    }
};


