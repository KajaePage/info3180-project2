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
                <li class="form-field make">
                    <label>Make</label>
                    <input v-model="form.make" class="input" type="text" placeholder="Tesla" name = "make" size="28">
                </li>

                <li class="form-field model">
                    <label>Model</label>
                    <input v-model="form.model" class="input" type="text" placeholder="Model S" name = "model" size="28">
                </li>

                <li class="form-field color">
                    <label>Colour</label>
                    <input v-model="form.colour" class="input" type="text" placeholder="Red" name = "colour" size="28">
                </li>

                 <li class="form-field year">
                    <label>Year</label>
                    <input v-model="form.year" class="input" type="text" placeholder="2018" name = "year" size="28">
                </li>

                  <li class="form-field price">
                    <label>Price</label>
                    <input v-model="form.price" class="input" type="text" placeholder="62868" name = "price" size="28">
                </li>

                <li class="form-field type">
                    <label>Car Type</label>
                    <select v-model="form.car_type" class="input" type="text" placeholder="SUV" name = "car_type" >
                        <option value="SUV">SUV</option>
                        <option value="Truck">Truck</option>
                        <option value="Van">Van</option>
                        <option value="Hyibrid/Electric">Hybrid/Electric</option>
                        <option value="Convertable">Convertable</option>
                        <option value="Coupe">Coupe</option>
                        <option value="Wagon">Wagon</option>
                        <option value="Sedan">Sedan</option>
                        <option value="Sports Car">Sports Car</option>
                        <option value="Crossover">Crossover</option>
                        <option value="Diesel">Diesel</option>
                        <option value="Luxury Car">Luxury Car</option>
                    </select>
                </li>
                <li class="form-field transmission">
                    <label>Transmission</label>
                    <select v-model="form.transmission" name = "transmission">
                        <option value="Automatic"> Automatic</option>
                        <option value="Manual">Manual</option>
                    </select>
                </li>

                <li class="form-field des">
                    <label>Description</label>
                    <textarea v-model="form.desc" class="input" type="text" name = "desc" rows="4" cols="65"></textarea>
                </li>

                <li class="form-field up">
                    <label>Upload Photo</label>
                    <input type="file" accept="image/*" class="form-control-file" @change="updatePhoto($event.target.files)" id ="photo" name= "photo">
                </li>
            </ul>
            <button class = "buttonsave" id="submit" type="submit" value="submit" @click.prevent="uploadPhoto()"  style="background-color: #0fb881;"> Save</button>
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
            window.location.href = '/explore';
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