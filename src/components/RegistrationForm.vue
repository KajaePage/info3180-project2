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
                <li class="form-field">
                    <label>Username <span class="required">*</span></label>
                    <input v-model="form.username" class="input" type="text" placeholder="Text input" name = "username">
                </li>

                <li class="form-field">
                    <label>Password <span class="required">*</span></label>
                    <input v-model="form.password" class="input" type="text" placeholder="Text input" name = "password">
                </li>

                <li class="form-field">
                    <label>Name <span class="required">*</span></label>
                    <input v-model="form.name" class="input" type="text" placeholder="Text input" name = "name">
                </li>

                <li class="form-field">
                    <label>Location <span class="required">*</span></label>
                    <input v-model="form.locat" class="input" type="text" placeholder="Text input" name = "location">
                </li>

                <li class="form-field">
                    <label>Biography <span class="required">*</span></label>
                    <input v-model="form.bio" class="input" type="text" placeholder="Text input" name = "biography">
                </li>

                <li class="form-field">
                    <label>Email <span class="required">*</span></label>
                    <input v-model="form.email" class="input" type="email" placeholder="Text input" name = "email">
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