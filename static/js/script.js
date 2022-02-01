
// Admin Modal // 
const addAdminBtn = document.querySelector('.add-admin-btn');
const addAdminCloseBtn =  document.querySelector('.admin-modal-top-close');
const addAdminModal =  document.querySelector('.admin-modal')

addAdminBtn.addEventListener("click",() => {
    addAdminModal.classList.add('show-modal')
})

addAdminCloseBtn.addEventListener("click", ()=>{
    addAdminModal.classList.remove('show-modal')
})


// Delete Action Modal //
const DeleteBtn = document.querySelector('.delete-action');
const DeleteCloseBtn =  document.querySelector('.delete-modal-top-close');
const DeleteModal = document.querySelector('.delete-modal')
const DeleteCancelBtn = document.querySelector('.cancel-btn')


// DeleteBtns = document.getElementsByClassName("delete-action");
// for (var i = 0; i < DeleteBtns.length; i++) {
//     DeleteBtns[i].addEventListener("click", function() {
//     DeleteModal.classList.add('show-modal')
//     });
// }

DeleteBtn.addEventListener("click",() => {
    DeleteModal.classList.add('show-modal')
})

DeleteCloseBtn.addEventListener("click",() => {
    DeleteModal.classList.remove('show-modal')
})

DeleteCancelBtn.addEventListener("click",() => {
    DeleteModal.classList.remove('show-modal')
})


// Edit Modal // 
const EditBtn = document.querySelector('.edit-action');
const EditCloseBtn =  document.querySelector('.edit-modal-top-close');
const EditModal =  document.querySelector('.edit-modal')

EditBtn.addEventListener("click",() => {
    EditModal.classList.add('show-modal')
})

EditCloseBtn.addEventListener("click", ()=>{
    EditModal.classList.remove('show-modal')
})

// // Edit Action Modal //
// const EditBtn = document.querySelector('.edit-action')

// EditBtn.addEventListener("click",() => {
//     addAdminModal.classList.add('show-modal')
// })

// EditBtn.addEventListener("click", ()=>{
//     addAdminModal.classList.remove('show-modal')
// })


// Upload User Photo //
const upload_photo =  document.querySelector('#upload_photo');
var uploaded_image = "";

upload_photo.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploaded_image = reader.result;
        document.querySelector("#display_image").style.backgroundImage = 'url($uploaded_image})';
    });
    reader.readAsDataURL(this.files[0]);
})


//Notification close //
const NotifModal = document.querySelector('.notification-modal')
const NotifCloseBtn =  document.querySelector('.notification-modal-close');

NotifCloseBtn.addEventListener("click",() => {
    NotifModal.classList.add('hide-modal')
})

