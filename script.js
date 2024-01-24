let tg = window.Telegram.WebApp;
let buy = document.getElementById("buy");
let order = document.getElementById("order");
tg.expand();

buy.addEventListener("click", () => {
    document.getElementById("main").style.display = "none";
    document.getElementById("form").style.display = "block";
    document.getElementById("user_name").value = tg.initDataUnsafe.user.first_name + " " + tg.initDataUnsafe.user.last_name;
});

order.addEventListener("click", () => {
    document.getElementById("error").innerText = '';
    let name = document.getElementById("user_name").value;
    let email = document.getElementById("user_email").value;
    let phone = document.getElementById("user_phone").value;

    let validName = /^[A-Za-zА-Яа-я\s]+$/;
    let validEmail = /^\S+@\S+\.\S+$/;
    let validPhone = /^\+\d{11}$/;

    if (!validName.test(name)) {
        document.getElementById("error").innerText = 'Error in name';
        return;
    }
    if (!validEmail.test(email)) {
        document.getElementById("error").innerText = 'Error in email';
        return;
    }
    if (!validPhone.test(phone)) {
        document.getElementById("error").innerText = 'Error in phone number';
        return;
    }

    // Generate a random code
    let random10OffCode = generateRandomCodeFor10Off();

    // Display the code
    alert("10% Off your fist order\nCode: " + random10OffCode);

    let data = {
        name: name,
        email: email,
        phone: phone,
        code: random10OffCode
    }

    // Send data including the code
    tg.sendData(JSON.stringify(data));

    tg.close();
});

function generateRandomCodeFor10Off() {
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    let code = "";
    for (let i = 0; i < 8; i++) {
        code += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return code;
}
