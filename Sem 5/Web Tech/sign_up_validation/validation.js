// Regular expressions for field validation
const validationPatterns = {
  firstName: /^[a-zA-Z]{2,20}$/, // First name should contain only letters and be 2-20 characters long
  lastName: /^[a-zA-Z]{2,20}$/,  // Last name should contain only letters and be 2-20 characters long
  username: /^[a-z\d]{5,12}$/i,
  email: /^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/,
  password: /^[#\w@_-]{8,20}$/,
  telephone: /^\d{10}$/,
  gender: /^(male|female|other)$/, // Gender should be male, female, or other
  dob: /^\d{4}-\d{2}-\d{2}$/, // Date of birth should follow the yyyy-mm-dd format (HTML5 date input format)
  country: /^[a-zA-Z\s]{2,50}$/ // Country should contain only letters and spaces, and be 2-50 characters long
};

// Validate the input field against the corresponding regex
const validate = (field, regex) => {
  if (regex.test(field.value)) {
    field.classList.add('valid');
    field.classList.remove('invalid');
  } else {
    field.classList.add('invalid');
    field.classList.remove('valid');
  }
};

// Attach event listeners to all input fields
document.querySelectorAll('input, select').forEach(input => {
  const regex = validationPatterns[input.name];
  if (regex) {
    input.addEventListener('keyup', () => validate(input, regex));
    input.addEventListener('change', () => validate(input, regex)); // For select and date inputs
  }
});
