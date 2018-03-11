const dict = {
  uk: {
    custom: {
      name: {
        required: "Поле ім'я обов'язкове.",
      },
      email: {
        required: "Поле емейл обов'язкове.",
        email: "Некоректний емейл."
      },
      phone: {
        required: "Поле телефон обов'язкове.",
        phonenumber: "Некоректний номер телефону.",
      }
    }
  }
};
const config = {
  locale: 'uk',
  dictionary: dict 
}
VeeValidate.Validator.extend('phonenumber', {
  getMessage: field => 'Invalid phone number.',
  validate: value => {
    let plusregex = new RegExp('^[\+]')
    if (!plusregex.test(value)) {
      value = '+' + value
    } 
    let valid_number = libphonenumber.isValidNumber(value)
    if (valid_number) {
      return true
    }
    return false
  }
});
Vue.use(VeeValidate, config);

new Vue({
  delimiters: ['[[', ']]'],
  el: '#orderBooks',
  data: {
    title: '',
    bookId: '',
    price: '',
    orderPrice: '',
    name: '',
    email: '',
    phone: '',
    quantity: 1,
    message: '',
    submited: false
  },
  methods: {
    submitForm (event) {
      event.preventDefault()
      this.validateBeforeSubmit()
    },
    checkPlusNumber (phone) {
      let plus_regex = new RegExp('^[\+]')
      if (!plus_regex.test(phone)) {
        phone = '+' + phone
      }
      return phone
    },
    validateBeforeSubmit() {
      this.$validator.validateAll().then((result) => {
        if (result) {
          this.phone = this.checkPlusNumber(this.phone)
          this.sendOrder()
          return;
        }
      });
    },
    sendOrder () {
      axios.post('/en/books/create/order/', {
        name: this.name,
        book: this.bookId,
        email: this.email,
        phone: this.phone,
        message: this.message,
        quantity: this.quantity,
      })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      this.submited = true
    },
    substractQuantity() {
      if (this.quantity > 1) {
        this.quantity = this.quantity - 1
      }
    },
    setPrice () {
      this.orderPrice = this.price * this.quantity
    }
  }
})
