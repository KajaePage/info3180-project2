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
        <form method="POST" enctype="multipart/form-data" id = "RegistrationForm" @submit.prevent="uploadPhoto" class = "formc">
            <ul class="formstf">
                <li class="form-field1">
                    <label>Username</label>
                    <input v-model="form.username" class="input-user" type="text"  name = "username" size="28">
                </li>

                <li class="form-field2">
                    <label>Password</label>
                    <input v-model="form.password" class="input" type="text"  name = "password" size="28">
                </li>

                <li class="form-field3">
                    <label>Fullname</label>
                    <input v-model="form.name" class="input" type="text"  name = "name" size="28">
                </li>

                <li class="form-field4">
                    <label>Email</label>
                    <input v-model="form.email" class="input" type="email" name = "email" size="28">
                </li>

                <li class="form-field5">
                    <label>Location</label>
                    <input v-model="form.locat" class="input" type="text"  name = "location" size="28">
                </li>

                <li class="form-field6">
                    <label>Biography</label>
                    <textarea v-model="form.bio" class="input-bio"  name = "biography" rows="4" cols="65" ></textarea>
                </li>

                <li class="form-field7">
                    <label> Upload Photo</label>
                    <input type="file" accept="image/*" class="form-control-file photo" @change="updatePhoto($event.target.files)" id ="photo" name= "photo">
                    
                </li>
            </ul>
            <button class = "buttonreg"  id="submit" type="submit" value="submit" @click.prevent="uploadPhoto()" style="background-color: #0fb881;">Register</button>
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
              password: '',
              username: '',
              name: '',
              locat: '',
              bio: '',
              email: '',
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
      console.log(this.isValidJwt(this.token))
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
            let RegistrationForm = document.getElementById('RegistrationForm');
            let form_data = new FormData(RegistrationForm);
            form_data.append('photo',this.form.photo.data)
            fetch("/api/register", { 
                method : 'POST',
                headers: {
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