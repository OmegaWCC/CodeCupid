const poll_choices_container = document.getElementById('user_interests_container');
const add_more_fields = document.getElementById('add_more_fields');
const remove_fields = document.getElementById('remove_fields');


const placeholder_table = ["C++", "Python", "Hackathons", "Javascript", "Side Projects"];
add_more_fields.addEventListener("click", () => {

    const input_tags = poll_choices_container.getElementsByTagName('input');
    const newField = input_tags[0].cloneNode(true);
    
    newField.value = '';
    if (input_tags.length >= placeholder_table.length) {
        newField.placeholder = '';
    } else {
        newField.placeholder = placeholder_table[input_tags.length];
    }
    poll_choices_container.appendChild(newField);
});


remove_fields.addEventListener("click", () => {
	const input_tags = poll_choices_container.getElementsByTagName('input');
	if(input_tags.length >= 2) {
		poll_choices_container.removeChild(poll_choices_container.lastChild);
	}
});