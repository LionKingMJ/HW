var myBtn = document.querySelector('.yellow');
const text = document.querySelector('.active');
const text2 = document.querySelector('.active2');
myBtn.addEventListener('click', () => {
    const job = document.getElementById('input1').value;
    console.log(job);
    const time = document.getElementById('input2').value;
    console.log(time);
    text.innerHTML = '당신은'+ job + '전문가가 되기 위해서';
    text2.innerHTML = '대략' + Number(10000/time) + '일 이상 훈련하셔야 합니다 :)';
});