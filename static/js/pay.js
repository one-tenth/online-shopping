document.addEventListener('DOMContentLoaded', function() {
    
    
    // 获取两个浮动视窗元素
    var modal1 = document.getElementById("myModal1");
    var modal2 = document.getElementById("myModal2");

    // 获取两个图像元素
    var trans1Img = document.getElementById("trans-p");
    var trans2Img = document.getElementById("trans-2p");

    // 获取两个关闭按钮元素
    var span1 = document.querySelector("#myModal1 .close");
    var span2 = document.querySelector("#myModal2 .close");

    // 为第一个图像添加点击事件，显示第一个浮动视窗
    trans1Img.onclick = function() {
        modal1.style.display = "block";
    };

    // 为第二个图像添加点击事件，显示第二个浮动视窗
    trans2Img.onclick = function() {
        modal2.style.display = "block";
    };

    // 点击第一个浮动视窗的关闭按钮，关闭第一个浮动视窗
    span1.onclick = function() {
        modal1.style.display = "none";
    };

    // 点击第二个浮动视窗的关闭按钮，关闭第二个浮动视窗
    span2.onclick = function() {
        modal2.style.display = "none";
    };

    // 点击第一个浮动视窗外部，关闭第一个浮动视窗
    window.onclick = function(event) {
        if (event.target == modal1) {
            modal1.style.display = "none";
        }
        // 点击第二个浮动视窗外部，关闭第二个浮动视窗
        else if (event.target == modal2) {
            modal2.style.display = "none";
        }
    };
});
function updatePaymentMethod(method) {
    document.querySelector('.trans-2t').textContent = '付款方式:' + method;
}

function updateShippingMethod(method) {
    document.querySelector('.trans-t1').textContent = '寄送方式:' + method;
}