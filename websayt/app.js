// document.addEventListener("DOMContentLoaded", () => {
// const postForm = document.getElementById("post-form");
// const postContent = document.getElementById("post-content");
// const postList = document.getElementById("post-list");

// ```
// postForm.addEventListener("submit", (e) => {
//     e.preventDefault();

//     const content = postContent.value.trim();
//     if (content === "") return;

//     const postItem = document.createElement("div");
//     postItem.classList.add("post-item");
//     postItem.textContent = content;

//     postList.prepend(postItem);
//     postContent.value = "";
// });

// // Shu yerda keyinchalik backend bilan ulashamiz
// ```

// });

// Ro'yxatdan o'tish
async function registerUser(username, password) {
    const response = await fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    });
    const data = await response.json();
    console.log(data);
}

// Post qo'shish
async function addPost(user_id, content) {
    const response = await fetch('http://127.0.0.1:5000/add_post', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id, content })
    });
    const data = await response.json();
    console.log(data);
}

// Barcha postlarni olish va ko'rsatish
async function getPosts() {
    const response = await fetch('http://127.0.0.1:5000/posts');
    const posts = await response.json();
    console.log(posts);

    const postsDiv = document.getElementById('posts');
    postsDiv.innerHTML = '';
    posts.forEach(post => {
        const div = document.createElement('div');
        div.innerHTML = `<b>${post.username}</b>: ${post.content} <i>${post.created_at}</i>`;
        postsDiv.appendChild(div);
    });
}

// Sahifa yuklanganda barcha postlarni ko'rsatish
window.onload = getPosts;
