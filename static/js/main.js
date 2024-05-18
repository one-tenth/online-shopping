document.addEventListener('DOMContentLoaded', () => {
    const listImage = document.getElementById('list-p');
    const listP2 = document.getElementById('list-p2');
    const slidingMenu = document.getElementById('sliding-menu');

    listImage.addEventListener('click', () => {
        slidingMenu.classList.toggle('open'); // 切换菜单的显示状态
    });

    listP2.addEventListener('click', () => {
        slidingMenu.classList.remove('open'); // 关闭列表
    });
});
