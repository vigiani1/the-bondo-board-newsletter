const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));
app.use(express.json());

app.post('/order', (req, res) => {
    console.log('Order received:', req.body);
    res.json({ message: 'Order processed successfully' });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});