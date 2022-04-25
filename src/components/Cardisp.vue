<template>
<form @submit.prevent="searchNews" class="d-flex flex-column justify-content-center">
 <div class="input-group mx-sm-3 mb-2">
 <label class="visually-hidden" for="search">Search</label>
 <input type="search" name="search" v-model="searchTerm" id="search" class="form-control mb-2 mr-sm-2" placeholder="Enter search term here" />
 <input type="search" name="search" v-model="searchModel" id="search" class="form-control mb-2 mr-sm-2" placeholder="Enter search term here" />
 <button class="btn btn-primary mb-2" @click ="searchCars()">Search</button>
 </div>
 <p>You are searching for {{ searchTerm }}</p>
 </form>
 <ul class="news__list" v-if="!searched">
 <li  v-for="car in top3" class="news__item">
     
     <div class="card1">
      <img :src="getImgUrl(car.photo)" class="reset-this cimg"/>
     <div class="card1__details">
        <div class="ntitle">{{ car.year }} {{ car.make }}</div>
        <p class = "ndesc">{{car.model}}</p>
        <span class="tag">${{car.price}}</span>
         <input class = "pbut" id="pbut" type="button" value="View more details" @click.prevent="gotocar(car.id)"/>
     </div>
     </div>
</li>
</ul>
<ul class="news__list" v-else>
 <li  v-for="car in temp2" class="news__item">
     
     <div class="card1">
      <img :src="getImgUrl(car.photo)" class="reset-this cimg"/>
     <div class="card1__details">
        <div class="ntitle">{{ car.year }} {{ car.make }}</div>
        <p class = "ndesc">{{car.model}}</p>
        <span class="tag">${{car.price}}</span>
         <input class = "pbut" id="pbut" type="button" value="View more details" @click.prevent="gotocar(car.id)"/>
     </div>
     </div>
</li>
 </ul>
</template>

<script>
import shared from '@/shared'
export default {
    data() {
        return {
            carlist:[],
            temp:[],
            temp2:[],
            searchTerm: '',
            searchModel: '',
            searched: false
        };
    },
    mounted() {
    if (localStorage.token) {
      this.token = localStorage.token;
    }
    if (localStorage.username) {
      this.username = localStorage.username;
    }
    if (localStorage.user_id) {
      this.id = localStorage.user_id;
    }
    },
    created(){
        this.fgetCars()
        this.getCsrfToken();
        this.sanitize = shared.sanitize;
    },
    // watch: {
    //     checker() {
    //         this.carlist = this.carlist
    //     }
    //     },
    methods: {
        getImgUrl(pet) {
            return './uploads/' + pet
        },
        async fgetCars(){
            let self = this
            fetch('/api/cars', {
                method: 'GET',
                headers: {
                'Authorization': `Bearer: ${this.token}`,
                }
            })
            .then(function(response) {
            return response.json();
            })
            .then(function(data) {
                self.carlist = data.carlist;
            });
        },
        gotocar(cid)
          {
              this.$router.push({path: '/cars/${cid}'});
              localStorage.cid = cid;
              console.log(cid);
          },  
        
        searchCars() {
            let self = this;
            console.log('searched stuff')
            fetch('/api/search?make=' + this.sanitize(self.searchTerm) + "&model=" + this.sanitize(self.searchModel), {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer: ${this.token}`,
                }
                })
                .then(function(response) {
                    return response.json();
                })
                .then(function(data) {
                    console.log(data);
                    console.log('Pain')
                    self.temp2 = data.carlist;
                    self.searched = true
                });
        },
        getCsrfToken(){
            let self = this;
            fetch('/api/csrf-token')
            .then((response)=> response.json())
            .then((data) =>{
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        },
    },
    computed: {
        top3(){
            let self = this
            if (self.searchTerm || self.searchModel){
                console.log('check')
            }else{
                this.searched = false
                console.log('no search top 3')
                self.temp = self.carlist.map((x) => x);
                console.log(self.temp)
                return self.temp.splice(-3)
            }
        },
    }
    
    
}
</script>

<style>
.news__list{
    display: grid;
 
    grid-template-columns: repeat(3, 1fr);
    
    grid-auto-rows: auto;
    
    grid-gap: 1rem;
    
    list-style-type: none;
}
.card1 {

    background-color: white;
    border: 1px solid #bacdd8;
    padding: 8px;
    border-radius: 12px;
  }
.reset-this {
    animation : none;
    animation-delay : 0;
    animation-direction : normal;
    animation-duration : 0;
    animation-fill-mode : none;
    animation-iteration-count : 1;
    animation-name : none;
    animation-play-state : running;
    animation-timing-function : ease;
    backface-visibility : visible;
    background : 0;
    background-attachment : scroll;
    background-clip : border-box;
    background-color : transparent;
    background-image : none;
    background-origin : padding-box;
    background-position : 0 0;
    background-position-x : 0;
    background-position-y : 0;
    background-repeat : repeat;
    background-size : auto auto;
    border : 0;
    border-style : none;
    border-width : medium;
    border-color : inherit;
    border-bottom : 0;
    border-bottom-color : inherit;
    border-bottom-left-radius : 0;
    border-bottom-right-radius : 0;
    border-bottom-style : none;
    border-bottom-width : medium;
    border-collapse : separate;
    border-image : none;
    border-left : 0;
    border-left-color : inherit;
    border-left-style : none;
    border-left-width : medium;
    border-radius : 0;
    border-right : 0;
    border-right-color : inherit;
    border-right-style : none;
    border-right-width : medium;
    border-spacing : 0;
    border-top : 0;
    border-top-color : inherit;
    border-top-left-radius : 0;
    border-top-right-radius : 0;
    border-top-style : none;
    border-top-width : medium;
    bottom : auto;
    box-shadow : none;
    box-sizing : content-box;
    caption-side : top;
    clear : none;
    clip : auto;
    color : inherit;
    columns : auto;
    column-count : auto;
    column-fill : balance;
    column-gap : normal;
    column-rule : medium none currentColor;
    column-rule-color : currentColor;
    column-rule-style : none;
    column-rule-width : none;
    column-span : 1;
    column-width : auto;
    content : normal;
    counter-increment : none;
    counter-reset : none;
    cursor : auto;
    direction : ltr;
    display : inline;
    empty-cells : show;
    float : none;
    font : normal;
    font-family : inherit;
    font-size : medium;
    font-style : normal;
    font-variant : normal;
    font-weight : normal;
    height : auto;
    hyphens : none;
    left : auto;
    letter-spacing : normal;
    line-height : normal;
    list-style : none;
    list-style-image : none;
    list-style-position : outside;
    list-style-type : disc;
    margin : 0;
    margin-bottom : 0;
    margin-left : 0;
    margin-right : 0;
    margin-top : 0;
    max-height : none;
    max-width : none;
    min-height : 0;
    min-width : 0;
    opacity : 1;
    orphans : 0;
    outline : 0;
    outline-color : invert;
    outline-style : none;
    outline-width : medium;
    overflow : visible;
    overflow-x : visible;
    overflow-y : visible;
    padding : 0;
    padding-bottom : 0;
    padding-left : 0;
    padding-right : 0;
    padding-top : 0;
    page-break-after : auto;
    page-break-before : auto;
    page-break-inside : auto;
    perspective : none;
    perspective-origin : 50% 50%;
    position : static;
    /* May need to alter quotes for different locales (e.g fr) */
    quotes : '\201C' '\201D' '\2018' '\2019';
    right : auto;
    tab-size : 8;
    table-layout : auto;
    text-align : inherit;
    text-align-last : auto;
    text-decoration : none;
    text-decoration-color : inherit;
    text-decoration-line : none;
    text-decoration-style : solid;
    text-indent : 0;
    text-shadow : none;
    text-transform : none;
    top : auto;
    transform : none;
    transform-style : flat;
    transition : none;
    transition-delay : 0s;
    transition-duration : 0s;
    transition-property : none;
    transition-timing-function : ease;
    unicode-bidi : normal;
    vertical-align : baseline;
    visibility : visible;
    white-space : normal;
    widows : 0;
    width : auto;
    word-spacing : normal;
    z-index : auto;
    /* basic modern patch */
    all: initial;
    all: unset;
}

.cimg{
    width: 100%;
    height: 214px;
    object-fit: cover;
}

.ntitle {
    font-size: 24px;
    font-weight: 600;
  
    margin-top: 16px;
  }

.tag {
    padding: 4px 8px;
    border: 1px solid #e5eaed;
  
    border-radius: 50px;
    font-size: 12px;
    font-weight: 600;
    color: #788697;
    margin-bottom: 160px;
  }

  .ndesc {
    font-size: 14px;
    color: #7f8c9b;
    
  }

  .pbut {
    border: none;
    padding: 12px 24px;
    border-radius: 50px;
  
    font-weight: 600;
    color: #0077ff;
    background-color: #e0efff;
  

    margin: 15px auto;
    display: block;
    text-align: center;
  
    cursor: pointer;
    text-decoration: none;
  }

</style>