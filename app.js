
document.getElementById('switch-lang').addEventListener('click', function() {
    let currentLang = document.documentElement.lang;
    if (currentLang === 'ar') {
        document.documentElement.lang = 'en';
        document.getElementById('title').textContent = 'Login';
        document.querySelector('label[for="phone-number"]').textContent = 'Phone Number:';
        document.getElementById('submit-btn').textContent = 'Confirm';
        document.getElementById('switch-lang').textContent = 'AR';
    } else {
        document.documentElement.lang = 'ar';
        document.getElementById('title').textContent = 'تسجيل الدخول';
        document.querySelector('label[for="phone-number"]').textContent = 'رقم الهاتف:';
        document.getElementById('submit-btn').textContent = 'تأكيد';
        document.getElementById('switch-lang').textContent = 'EN';
    }
});
