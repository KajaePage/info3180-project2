<template>
<form @submit.prevent="searchNews" class="d-flex flex-column justify-content-center">
 <div class="input-group mx-sm-3 mb-2">
 <label class="visually-hidden" for="search">Search</label>
 <input type="search" name="search" v-model="searchTerm" id="search" class="form-control mb-2 mr-sm-2" placeholder="Enter search term here" />
 <input type="search" name="search" v-model="searchModel" id="search" class="form-control mb-2 mr-sm-2" placeholder="Enter search term here" />
 <button class="btn btn-primary mb-2">Search</button>
 </div>
 <p>You are searching for {{ searchTerm }}</p>
 </form>
 <ul class="news__list">
 <li v-for="car in top3" class="news__item">
     
     <div class="card">
      <img :src="getImgUrl(car.photo)"/>
     <div class="card__details">
        <div class="ntitle">{{ car.make }}</div>
        <p class = "ndesc">{{car.desc}}</p>
         <input class = "pbut" id="pbut" type="button" value="submit" @click.prevent="uploadPhoto()"/>
     </div>
     </div>
     </li>
 </ul>
</template>

<script>
export default {
    data() {
        return {
            carlist:[],
            temp:[],
            searchTerm: '',
            searchModel: ''
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
        
        searchNews() {
            let self = this;
            fetch('https://newsapi.org/v2/everything?q='+self.searchTerm + '&language=en', {
            headers: {
            'Authorization': `Bearer ${import.meta.env.VITE_NEWSAPI_TOKEN}`,
            }
            })
            .then(function(response) {
            return response.json();
            })
            .then(function(data) {
                console.log(data);
                self.carlist = data.carlist;
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
            if (self.searchTerm){
                console.log('searched stuff')
                fetch('/api/cars?st=' + self.searchTerm, {
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
                        console.log(data);
                        console.log('Pain')
                        self.temp = data.carlist;
                    });
                return self.carlist
            }else{
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
.card {

    background-color: white;
    border: 1px solid #bacdd8;
    padding: 8px;
    border-radius: 12px;
  }

.news__list li img{
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