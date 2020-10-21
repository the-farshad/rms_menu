var app = new Vue({
    el: '#app',
    mounted() {
        let vm = this
        axios
            .get(
                'https://sheets.googleapis.com/v4/spreadsheets/1BNa_eMZo-BvXUBbzVJewlpjqzXatReSzl52aYfoWpdU/values/Specials!A2:D183?key=AIzaSyBhiqVypmyLHYPmqZYtvdSvxEopcLZBdYU'
            )
            .then(function (response) {
                let specials = response.data.values
                for (let index = 0; index < specials.length; index++) {
                    const element = specials[index]
                    let mitem = {
                        name: element[0],
                        description: element[1],
                        price: element[2],
                        image: element[3],
                    }

                    vm.menuItems_L = vm.menuItems_L.concat(mitem)
                }
                console.log(response)
            })
    },
    data: {
        menuItems_L: [],
        menuItems_R: [],
        menuStyle: {
            background: '#ffe6d1',
            color: '#000'
        },
        dotStyle: {
            backgroundImage: 'radial-gradient(' + this.color + ' 1px, transparent 0px)'
        }
    },
    computed: {},
    methods: {
        isEven: function (n) {
            return n % 2 == 0
        }
    }
});