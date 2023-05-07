const star = document.querySelector('#star-check')
const rating = document.querySelector('#rating')

$(document).ready(function() {
  var left = 0
  var right = 0
  var isclick = 0
  var clicked = 0
  
  // Add click event to the SVG tags
  $('.clickable-star').on('click', function(event) {
    // Get the current SVG tag's ID
    var id = $(this).attr('id')
    var x = event.pageX - $(this).offset().left
    isclick = 1
    
    if (id == 'star-1') {
      left = 1
      right = 2
    } else if (id == 'star-2') {
      left = 3
      right = 4
    } else if (id == 'star-3') {
      left = 5
      right = 6
    } else if (id == 'star-4') {
      left = 7
      right = 8
    } else if (id == 'star-5') {
      left = 9
      right = 10
    }

    if (x < $(this).width() / 2) {
      star.classList.add(`star-check-${left}`);
      clicked = left
      rating.setAttribute('value', `${left/2}`)
    } else {
      star.classList.add(`star-check-${right}`);
      clicked = right
      rating.setAttribute('value', `${left/2}`)
    }
  });
  
  // Add mouseover event to the SVG tags
  $('.clickable-star').on('mouseover', function(event) {
    // Get the current mouse position relative to the SVG tag
    star.className = ""
    var id = $(this).attr('id')
    var x = event.pageX - $(this).offset().left

    if (id == 'star-1') {
      left = 1
      right = 2
    } else if (id == 'star-2') {
      left = 3
      right = 4
    } else if (id == 'star-3') {
      left = 5
      right = 6
    } else if (id == 'star-4') {
      left = 7
      right = 8
    } else if (id == 'star-5') {
      left = 9
      right = 10
    }
    
    if (x < $(this).width() / 2) {
      star.classList.add(`star-check-${left}`)
    } else {
      star.classList.add(`star-check-${right}`)
    }
  });

  $('.clickable-star').on('mouseout', function(event) {
    star.className = ""
    if (isclick) {
      star.classList.add(`star-check-${clicked}`)
    } else {
      star.classList.add('star-check-0')
    }
  });
});

// 모든 라디오 버튼과 해당 라벨 요소를 가져옴
const radios_taste = document.querySelectorAll('[name="rating_taste"]')
const labels_taste = document.querySelectorAll('label.labels_taste')
const radios_price = document.querySelectorAll('[name="rating_price"]')
const labels_price = document.querySelectorAll('label.labels_price')
const radios_kind = document.querySelectorAll('[name="rating_kind"]')
const labels_kind = document.querySelectorAll('label.labels_kind')

const radioGroups = [
  { radios: radios_taste, labels: labels_taste },
  { radios: radios_price, labels: labels_price },
  { radios: radios_kind, labels: labels_kind },
];

// 라디오 버튼에 이벤트 리스너 추가
radioGroups.forEach(radioGroup  => {
  const radios = radioGroup.radios
  const labels = radioGroup.labels
  radios.forEach(radio => {
    const resultBtn = document.querySelector(`.btn_${radio.getAttribute('name')}`)
    radio.addEventListener('change', event => {
      // 선택된 라디오 버튼의 인덱스 가져오기
      const selectedRadioIndex = Array.prototype.indexOf.call(radios, event.target);
      const selectedLabelText = labels[selectedRadioIndex].textContent
      // 해당 라벨 요소의 스타일 변경
      labels.forEach((label, index) => {
        if (index === selectedRadioIndex) {
          label.style.color = '#0ac7ce' // 선택된 라디오 버튼의 라벨 색상 변경
        } else {
          label.style.color = 'initial' // 선택되지 않은 라디오 버튼의 라벨 색상 초기화
        }
      });
      resultBtn.textContent = selectedLabelText
      resultBtn.setAttribute('style', 'background-color: #0ac7ce; border: none; width: 88px;')
    });
  });
});

// 태그 인풋 선택
const purposeTags = document.getElementById('purpose-tags')
const atmosphereTags = document.getElementById('atmosphere-tags')
const facilityTags = document.getElementById('facility-tags')

const purposeButtons = document.querySelectorAll('.purpose-button')
const atmosphereButtons = document.querySelectorAll('.atmosphere-button')
const facilityButtons = document.querySelectorAll('.facility-button')

const buttons = [purposeButtons, atmosphereButtons, facilityButtons]

function updateTagsField() {
  const selectedPurposeTagIds = []
  const selectedAtmosphereTagIds = []
  const selectedFacilityTagIds = []

  purposeButtons.forEach(tagBtn => {
    if (tagBtn.classList.contains('selected')) {
      const tagId = Number(tagBtn.dataset.tag)
      selectedPurposeTagIds.push(tagId)
    }
  })

  atmosphereButtons.forEach(tagBtn => {
    if (tagBtn.classList.contains('selected')) {
      const tagId = Number(tagBtn.dataset.tag)
      selectedAtmosphereTagIds.push(tagId)
    }
  })

  facilityButtons.forEach(tagBtn => {
    if (tagBtn.classList.contains('selected')) {
      const tagId = Number(tagBtn.dataset.tag)
      selectedFacilityTagIds.push(tagId)
    }
  })

  purposeTags.value = selectedPurposeTagIds.join(',')
  atmosphereTags.value = selectedAtmosphereTagIds.join(',')
  facilityTags.value = selectedFacilityTagIds.join(',')
  console.log(purposeTags.value);
  console.log(atmosphereTags.value);
  console.log(facilityTags.value);
}

buttons.forEach(buttons=> {
  buttons.forEach(button => {
    button.addEventListener('click', event => {
      event.preventDefault() // 이벤트 전파 중지
      button.classList.toggle('selected')
      if (button.classList.contains('btn-outline-dark')) {
        button.classList.remove('btn-outline-dark')
        button.classList.add('btn-primary')
      } else if (button.classList.contains('btn-primary')) {
        button.classList.remove('btn-primary')
        button.classList.add('btn-outline-dark')
      }
      updateTagsField()
      event.stopPropagation() // 이벤트 전파 중지
    })
  })
})

// const form = document.querySelector('form')
// form.addEventListener('submit', () => {
//   buttons.forEach((buttons, index) => {
//     updateTagsField()
//   })
// })