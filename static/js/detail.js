const menuAddBtn = document.querySelector('.menu-add')
const menuFormDiv = document.querySelector('.menu-form')
const menuForm = document.querySelector('#menu-form')

menuAddBtn.addEventListener('click', (event) => {
  menuFormDiv.setAttribute('style', '')
  menuAddBtn.setAttribute('style', 'display:none')
})

menuForm.addEventListener('submit', function(event) {
  event.preventDefault()

  // 폼 데이터 가져오기
  const formData = new FormData(menuForm)
  const diningId = event.target.dataset.diningId
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  axios({
    method: 'post',
    url: `/dinings/${diningId}/menus`,
    headers: {'X-CSRFToken': csrftoken,},
    data: formData
  })
  .then(response => {
    const menu = response.data;

    const menuElement = document.createElement('div');
    menuElement.className = 'd-flex justify-content-between';
    menuElement.innerHTML = `
      <p>${menu.name}</p>
      <p>${menu.price}</p>
    `;

    // 새로운 메뉴 요소를 버튼 위에 삽입
    menuAddBtn.insertAdjacentElement('beforebegin', menuElement);
    menuFormDiv.style.display = 'none';
    menuAddBtn.style.display = '';

    // 입력 필드 초기화
    menuForm.reset();
  })
})


const likeForm = document.querySelector('#like-form')

likeForm.addEventListener('submit', function (event) {
  event.preventDefault()

  const diningsId = event.target.dataset.diningsId
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  

  axios({
    method: 'post',
    url: `/dinings/${diningsId}/likes/`,
    headers: {'X-CSRFToken': csrftoken},
  })
  .then((response) => {
    const isLiked = response.data.is_liked
    // const likeBtn = document.querySelector('button > i')
    const likeCount = document.querySelector('#like_count')

    // 클릭한 버튼 선택
    const likeBtn = event.target;
    // 버튼 내부의 i 태그를 선택
    const likeIcon = likeBtn.querySelector('i');

    likeCount.textContent = `(${response.data.like_count})`
    if (isLiked) {
      // console.log(likeBtn.classList, 1)
      // likeBtn.className = 'bi bi-heart-fill'
      likeIcon.classList.remove('bi-heart');
      likeIcon.classList.add('bi-heart-fill');
    } else {
      // console.log(likeBtn.classList, 2)
      // likeBtn.className = 'bi bi-heart'
      likeIcon.classList.remove('bi-heart-fill');
      likeIcon.classList.add('bi-heart');
    }
    console.log(likeBtn)

  })
})


const tagLinks = document.querySelectorAll('.search-tag');
tagLinks.forEach(link => {
  link.addEventListener('click', function(event) {
    event.preventDefault();
    const tag = this.dataset.tag;
    const url = `/dinings/search/?query=${tag}`;
    window.location.href = url;
  });
});