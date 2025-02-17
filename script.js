document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('designCanvas');
    const ctx = canvas.getContext('2d');
    document.getElementById('uploadImage').addEventListener('click', () => {
        alert('Upload Image Clicked');
    });
    document.getElementById('addText').addEventListener('click', () => {
        ctx.fillText('Sample Text', 50, 50);
    });
    document.getElementById('saveDesign').addEventListener('click', () => {
        alert('Design Saved');
    });
    document.getElementById('placeOrder').addEventListener('click', () => {
        alert('Order Placed');
    });
});