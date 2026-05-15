function renderAuthUI(){

    const box = document.getElementById("userBox");
    if(!box) return;

    const user = JSON.parse(sessionStorage.getItem("user"));

    if(user){
        box.innerHTML = `
            <span id="userName" style="cursor:pointer; font-weight:600; color:#ffd6de;">
                Welcome ${user.name} ▼
            </span>
            <div id="logoutBox" style="display:none; margin-top:5px;">
                <button onclick="logout()" style="
                    background:#ffb6c1;
                    border:none;
                    padding:6px 12px;
                    border-radius:20px;
                    cursor:pointer;
                ">
                    Logout
                </button>
            </div>
        `;

        document.getElementById("userName").onclick = function(){
            const box = document.getElementById("logoutBox");
            box.style.display = box.style.display === "none" ? "block" : "none";
        };

    } else {
        box.innerHTML = `<a href="/login" style="color:white;">Login</a>`;
    }
}

function logout(){
    sessionStorage.removeItem("user");
    window.location.href = "/";
}

// IMPORTANT: run on every page load
window.addEventListener("load", renderAuthUI);