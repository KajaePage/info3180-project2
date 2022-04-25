<template>
<!-- <div class="userdata">
    <a>{{display}}</a>
</div>    -->
<div class="card2 mb-3" >
    <div class="row no-gutters">
      <div class="col-md-4 card__media">
        <img :src="getImgUrl(display.photo)" class="reset-this cimg">
      </div>
      <div class="col-md-8">
        <div class="card-body">
            <h5 class="card-title">{{display.year}} {{display.make}}</h5>
            <p class = "ndesc">{{car.model}}</p>
            <p class="card-text">{{display.desc}}</p>
            <div class = "tags">
                <span class="tag">Price: ${{display.price}}</span>
                <span class="tag">Body Type: {{display.car_type}}  </span>
            </div>
            
            
            <div class="rbth">
                <span class="tag">Colour:  <span> {{display.colour}}</span>   </span>
                <span class="tag">Transmission: {{display.transmission}} </span>
            </div>
            <div class = "bhold">
                <button class="pbut">Email Owner</button>
                <button class="pbut" @click="add_to_fav()">Add to Fav</button>
            </div>
            
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default 
{
    data() {
    return {
        car:{},
        url: ''
    };
    },
    created() {
        let self = this
        this.getCsrfToken();
        this.fgetsCars()
    },
        computed:
    {
       display: function() 
       {
           return this.car;
       }
    },
    mounted() {
     window.onbeforeunload = () => {
    }    
    if (localStorage.token) {
      this.token = localStorage.token;
      console.log(this.token)
    }
    if (localStorage.username) {
      this.username = localStorage.username;
    }
    },
    methods: {
        getImgUrl(pet) {
            self.url = '../uploads/' + pet
            if (! url) {
                return ''; //or perhaps a placeholder loading image 
            }
            return self.url
        },
        async fgetsCars(){
            let self = this
            fetch("/api/cars/<car_id>?id="+localStorage.cid,
        {method: 'GET',headers: {'Authorization': `Bearer: ${localStorage.token}`}})
            .then(function (response) {
                return response.json();
            })
        .then(function (data) {
            // display a success message
            self.car = data["car_data"]
            console.log(self.car);
        })
        .catch(function (error) {
            console.log(error);
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
        add_to_fav(){
            fetch('/api/cars/<car_id>/favourite?car_id=' + localStorage.cid, {
                method: 'POST',
                headers: {
                'Authorization': `Bearer: ${this.token}`,
                'X-CSRF-TOKEN': this.csrf_token
                }
            })
            .then(function(response) {
            return response.json();
            })
            .then(function(data) {
                console.log(data)
                self.carlist = data.carlist;
            });
        }
    }
}
</script>

<style>



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
    .plist{
    display: grid;
 
    grid-template-columns: repeat(3, 1fr);
    
    grid-auto-rows: auto;
    
    grid-gap: 1rem;
    
    list-style-type: none;
}

.card__media {
  position: relative;
  width: 512px;
}

.card__media img {
  display: block;
  max-width: 100%;
  height: 100%;
}

.card2 {

    background-color: white;
    border: 1px solid #bacdd8;
    padding: 8px;
    border-radius: 12px;
  }

.cimg{
    width: 100%;
    height: 214px;
    object-fit: cover;
}

.pname {
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

  .plocat {
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

  .card-text {
    margin-top:10px;
  }

  .card.mb-3{
    max-width: 100%; 
    height: 2fr;
  }

  .card-img{
    width: 100%;
  }

  .col-md-4{
    max-width: 60%;
  }

  .rbth {
    margin-bottom: 10px;
  }
  .card-body .pbut{
    display: inline;
  }

  .card__details {
    padding: 16px 8px 8px 8px;
  }

</style>