<template>
<div class="userdata">
    <div class="card mb-3" >
    <div class="row no-gutters">
      <div class="col-md-4">
        <img :src="getImgUrl(display.photo)" class="card-img">
      </div>
      <div class="col-md-8">
        <div class="card-body">
            <h1 class="card-title">{{display.name}}</h1>
            <h3 class="card-title">@{{display.username}}</h3>
            <p class="card-text">{{display.biography}}</p>
            <p class="card-text">Email: {{display.email}}</p>
            <p class="card-text">Location: {{display.location}}</p>
            <p class="card-text">Joined: {{display.date_joined}}</p>    
        </div>
      </div>
    </div>
  </div>

     <ul class="news__list">
    <li  v-for="car in cardisplay" class="news__item">
     
     <div class="card">
      <img :src="getImgUrl(car.photo)"/>
     <div class="card__details">
        <div class="ntitle">{{ car.year }} {{ car.make }}</div>
        <p class = "ndesc">{{car.model}}</p>
         <input class = "pbut" id="pbut" type="button" value="submit" @click.prevent="gotocar(car.id)"/>
     </div>
     </div>
    </li>
    </ul>
    </div>  
         
</template>

<script>
export default 
{
    data() {
    return {
        user_id: localStorage.user_id,
        userdict:{},
        carlist:null,
        url:''
    };
    },
    created() {
        let self = this
        fetch("/api/users/<user_id>?id="+localStorage.user_id,
         {method: 'GET',headers: {'Authorization': `Bearer: ${localStorage.token}`}})
            .then(function (response) {
                return response.json();
            })
        .then(function (data) {
            // display a success message
            self.userdict = data["user_data"]
            console.log(self.userdict);
        })
        .catch(function (error) {
            console.log(error);
        });
        fetch("/api/users/<user_id>/favourites?id="+localStorage.user_id,
         {method: 'GET',headers: {'Authorization': `Bearer: ${localStorage.token}`}})
            .then(function (response) {
                console.log('here')
                return response.json();
            })
        .then(function (data) {
            // display a success message
            self.carlist = data["favdata"]
            console.log(self.carlist);
        })
        .catch(function (error) {
            console.log(error);
        });
    },
        computed:
    {
       display: function() 
       {
           return this.userdict;
       },
       cardisplay: function()
       {
           return this.carlist;
       },
       gotocar(cid)
          {
              this.$router.push({path: '/cars/${cid}'});
              localStorage.cid = cid;
              console.log(cid);
          },  
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
    methods:{
        getImgUrl(pet) {
            self.url = '../uploads/' + pet
            if (! url) {
                return ''; //or perhaps a placeholder loading image 
            }
            return self.url
        }    
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