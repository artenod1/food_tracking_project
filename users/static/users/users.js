formButton = document.querySelector('#form-button')

formButton.addEventListener('click', function () {
	if(document.querySelector('#profile-form').style.display === 'block'){
		document.querySelector('#profile-form').style.display = 'none';
	}
	else{
		document.querySelector('#profile-form').style.display = 'block'
	}
});