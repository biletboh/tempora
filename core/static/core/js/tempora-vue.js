const dict = {
  uk: {
    custom: {
      name: {
        required: "Поле ПІБ обов'язкове.",
      },
      email: {
        required: "Поле емейл обов'язкове.",
        email: "Некоректний емейл."
      },
      phone: {
        required: "Поле телефон обов'язкове.",
        phonenumber: "Некоректний номер телефону.",
      },
      address: {
        required: "Вкажіть адресу доставки (наприклад, відділення 'Нової пошти').",
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
    address: '',
    quantity: 1,
    message: '',
    submited: false,
    selected: 1,
    bestSeller: 1,
    newBooks: 1,
    selectedIsActive: false,
    bestSellerIsActive: false,
    newBooksIsActive: false,
    category: 'Категорії',
    categoryValue: [],
  },
  created: function() {
    this.getFilterData();
  },
  mounted: function() {
    this.okSize();
  },
  methods: {
    okSize() {
      for (ref in this.$refs) {
        let img = this.$refs[ref].children[0];
        let mask = this.$refs[ref].children[1];
        if (img.clientHeight < 450 || img.clientWidth < 300) {
          this.$refs[ref].removeChild(mask);
        }
      }
    },
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
        address: this.address,
        quantity: this.quantity,
      })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      this.submited = true
      this.clearUpOrderData()
    },
    clearUpOrderData () {
      console.log('test', this.bookId);
      this.name = '',
      this.bookId = '',
      this.email = '',
      this.phone = '',
      this.message = '',
      this.price = '',
      this.orderPrice = '',
      this.address = '',
      this.quantity = 1 
      console.log('test after', this.bookId);
    },
    substractQuantity() {
      if (this.quantity > 1) {
        this.quantity = this.quantity - 1
      }
    },
    setPrice () {
      this.orderPrice = this.price * this.quantity
      console.log('test after price', this.bookId);
    },
    getFilterData() {
      let query = this.$route.query
      if (query.new && query.new === '2') {
        this.newBooks = 2 
        this.newBooksIsActive = true 
      }
      if (query.selected && query.selected === '2') {
        this.selected = 2 
        this.selectedIsActive = true 
      }
      if (query.best_seller && query.best_seller === '2') {
        this.bestSeller = 2 
        this.bestSellerIsActive = true 
      }
      if (query.tags) {
        for (var i=0; i < query.tags.length; i++) {
          this.categoryValue.push(query.tags[i])
        }
      }
    },
    setNewBooksFilterValue () {
      if (this.newBooks === 2) {
        this.newBooks = 1 
        this.newBooksIsActive = false 
      } else {
        this.newBooks = 2 
        this.newBooksIsActive = true 
      }
    },
    setBestSellerFilterValue () {
      if (this.bestSeller === 2) {
        this.bestSeller = 1 
        this.bestSellerIsActive = false 
      } else {
        this.bestSeller = 2 
        this.bestSellerIsActive = true 
      }
    },
    setSelectedFilterValue () {
      if (this.selected === 2) {
        this.selected = 1 
        this.selectedIsActive = false
      } else {
        this.selected = 2 
        this.selectedIsActive = true 
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
