<template>
    <div class = "container">
        <div v-if="response.errors != 'novalue'" class = "error-message">
            <ul id="vlist">
                <li v-for="(error, index) in response.errors">
                    {{ error }}
                </li>
            </ul>
        </div>
        <div v-if="response.message != 'novalue'" class = "success-message">
            {{response.message}}
        </div>
        <form method="POST" enctype="multipart/form-data" id = "CarForm" @submit.prevent="uploadPhoto" class = "formc">
            <ul class="formstf">
                <li class="form-field">
                    <label>Make <span class="required">*</span></label>
                    <input v-model="form.make" class="input" type="text" placeholder="Text input" name = "make">
                </li>

                <li class="form-field">
                    <label>model <span class="required">*</span></label>
                    <input v-model="form.model" class="input" type="text" placeholder="Text input" name = "model">
                </li>

                <li class="form-field">
                    <label>colour <span class="required">*</span></label>
                    <input v-model="form.colour" class="input" type="text" placeholder="Text input" name = "colour">
                </li>

                <li class="form-field">
                    <label>transmission <span class="required">*</span></label>
                    <input v-model="form.transmission" class="input" type="text" placeholder="Text input" name = "transmission">
                </li>

                <li class="form-field">
                    <label>year <span class="required">*</span></label>
                    <input v-model="form.year" class="input" type="text" placeholder="Text input" name = "year">
                </li>

                <li class="form-field">
                    <label>description <span class="required">*</span></label>
                    <input v-model="form.desc" class="input" type="text" placeholder="Text input" name = "desc">
                </li>
                <li class="form-field">
                    <label>type <span class="required">*</span></label>
                    <input v-model="form.car_type" class="input" type="text" placeholder="Text input" name = "car_type">
                </li>

                <li class="form-field">
                    <label>price <span class="required">*</span></label>
                    <input v-model="form.price" class="input" type="text" placeholder="Text input" name = "price">
                </li>

                <li class="form-field">
                    <label>Photo <span class="required">*</span></label>
                    <input type="file" accept="image/*" class="form-control-file" @change="updatePhoto($event.target.files)" id ="photo" name= "photo">
                </li>
            </ul>
            <input class = "button" id="submit" type="submit" value="submit" @click.prevent="uploadPhoto()"/>
        </form> 
    </div>
</template>

<script>
import shared from '@/shared'
export default {
    data() {
      return {
          response: {},
          csrf_token: '',
          form:{
              Make: '',
              model: '',
              colour: '',
              transmission: '',
              year: '',
              desc: '',
              car_type: '',
              price: '',
              photo: {}
          }
      }        
    },
    created() {
        this.getCsrfToken();
        this.isValidJwt = shared.isValidJwt;
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
    methods:{
        updatePhoto(files){
            console.log(files[0])
                if (!files.length){
                    console.log("??")
                    return;
                } 
                

                this.form.photo = {
                    name: files[0].name,
                    data: files[0]
                };
            },
        uploadPhoto(){
            let self = this
            let CarForm = document.getElementById('CarForm');
            let form_data = new FormData(CarForm);
            form_data.append('photo',this.form.photo.data)
            fetch("/api/cars", { 
                method : 'POST',
                headers: {
                    'Authorization': `Bearer: ${this.token}`,
                    'X-CSRF-TOKEN': this.csrf_token
                },
                body: form_data
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
            // display a success message
            self.response = data;
            console.log(data);
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
        containskey(obj, key){
            return Object.keys(obj).includes(key)
        }
         
    },
    computed: {
        haserr() {
            return this.containsKey(this.response, 'errors');
        },
        hasmsg() {
            return this.containsKey(this.response, 'errors');
        }
    }
    

    
}
</script>

<style>
 /* feel free to kill this 
 Temporarily here so that my eyes dont bleed while testing code*/
 .formc{
    margin:10px auto;
    max-width: 400px;
    padding: 20px 12px 10px 20px;
    font: 13px "Lucida Sans Unicode", "Lucida Grande", sans-serif;
  }
  .formc li {
    padding: 0;
    display: block;
    list-style: none;
    margin: 10px 0 0 0;
  }
  .formc label{
    margin:0 0 3px 0;
    padding:0px;
    display:block;
    font-weight: bold;
  }
  
  .formc input,textarea{
      box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    border:1px solid #BEBEBE;
    padding: 7px;
    margin:0px;
    outline: none;
      width: 100%;
  }
  
  .formc textarea{
    height: 100px;
      width: 100%;
  }
  
  .formc .required{
    color:red;
  }
  
  .formc label{
      width:80%;
  }
  
 .formc .button{
      background: #2f4ad0;
      border: none;
      padding: 8px 15px 8px 15px;
    border: none;
      color:white;
  }

  .error-message{
      background-color: #F8D7DA;
      color: #701A22;
  }

  .success-message{
      background-color:#D4EDDA;
      color: #3D7553;
  }
</style>