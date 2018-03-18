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

const router = new VueRouter({
    mode: 'history',
    routes: []
});

new Vue({
  delimiters: ['[[', ']]'],
  el: '#orderBooks',
  router,
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
    submited: false,
    selected: false,
    bestSeller: false,
    newBooks: false,
    category: 'Категорії',
    categoryValue: [],
  },
  created: function() {
    this.getFilterData();
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
    },
    getFilterData() {
      let query = this.$route.query
      if (query.new && query.new === 'on') {
        this.newBooks = true
      }
      if (query.selected && query.selected === 'on') {
        this.selected = true
      }
      if (query.best_seller && query.best_seller === 'on') {
        this.bestSeller = true
      }
      if (query.tags) {
        for (var i=0; i < query.tags.length; i++) {
          this.categoryValue.push(query.tags[i])
        }
      }
    },
    setNewBooksFilterValue () {
      if (this.newBooks) {
        this.newBooks = false
      } else {
        this.newBooks = true
      }
    },
    setBestSellerFilterValue () {
      console.log('bestseller')
      if (this.bestSeller) {
        this.bestSeller = false
      } else {
        this.bestSeller = true
      }
    },
    setSelectedFilterValue () {
      if (this.selected) {
        this.selected = false
      } else {
        this.selected = true
      }
    },
    setCategory (value, category) {
      this.category = category 
      if (value) {
        this.categoryValue.push(value)
      } else {
        this.categoryValue = []
      }
    }
  }
})
