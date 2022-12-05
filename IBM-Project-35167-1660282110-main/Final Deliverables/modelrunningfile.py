from flask import Flask,request, url_for, redirect, render_template
import pickle
filename ='prediction_employee'
loaded_model= pickle.load(open(filename,'rb'))
app = Flask(__name__)
@app.route('/')
def hello_world():

    return render_template("login.html")






@app.route('/loginflask',methods=['POST','GET'])

def loginflask():
     dict={"it": 0,
      "sales": 7,
      "support": 8,
      "product_mng": 6,
      "marketing": 5,
      "hr": 3,
      "management": 4,
      "accounting": 2,
      "technical": 9}
     dict1={"high":0,"medium":2,"low":1}
     a0 = request.form["email"]
     a2 = request.form["email0"]
     a3 = request.form["email1"]
     a4 = request.form["email2"]
     a5 = request.form["email3"]
     a6 = request.form["email4"]
     a7 = request.form["email5"]
     a8 = request.form["email6"]
     a8=dict1[a8]
     a11 = request.form["email7"]
     a11=dict[a11]

     print(int(a0),int(a2),int(a3),int(a4),int(a5),int(a8),int(a11),float(a6),float(a7))
     a=[[10,240,8,4,2,0,0,0.3,0.9]]
     watagory=['Employee will stay','Employee will Leave']
     pred_result =loaded_model.predict(a)
     u=(int(pred_result))
     w="prediction "+watagory[u]
     q='''<form action="/loginflask" method ="post" >
      <br><br><br><br><input class="fname" type="text"  placeholder="Number of Project" name="email"> <br><br><br><br>
            <br><br><br><br><input type="text" placeholder="Average Montly Hours" name="email0">
           <br><br><br><br><input type="text"  placeholder="Time Spend in Company" name="email1">
           <br><br><br><br><input type="text"  placeholder="Work Accident" name="email2">
           <br><br><br><br><input type="text"  placeholder="promotion_last_5years" name="email3">


             <br><br><br><br><select  name="email6">
                  <option value="salary">choose salary</option>
    <option value="high">high</option>
    <option value="medium">medium</option>
    <option value="low">low</option></select>

                       <br><br><br><br><select name="email7">
                  <option value="salary">choose department</option>
    <option value="it">it</option>
    <option value="sales">sales</option>
    <option value="support">support</option>
                          <option value="product_mng">product_mng</option>
    <option value="marketing">marketing</option>
    <option value="hr">hr</option>
                          <option value="management">management</option>
    <option value="accounting">accounting</option>
    <option value="technical">technical</option></select>
                     <br><br><br><br><input type="text"  placeholder="satisfaction level" name="email4"><br><br><br><br>
           <br><br><br><br><input type="text" placeholder="last evaluation" name="email5">

         <br><br><br><br><button type="submit" href="/">Submit</button>
         </form>'''


     return render_template("login.html",q=q,w=w)



@app.route('/loginflask8',methods=['POST','GET'])

def loginflask8():
    q='<iframe src="https://us1.ca.analytics.ibm.com/bi/?perspective=dashboard&pathRef=.public_folders%2Femp%2Brelation%2Femp_pie_analysis&action=view&mode=dashboard&subView=model0000018471c7d1f6_00000000" width="1000" height="1000" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen=""></iframe>"'
    return render_template("login.html",q=q)
@app.route('/loginflask12',methods=['POST','GET'])

def loginflask12():
    q = '''<section class="vh-100" style="background-color: #9de2ff;">
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <section style="background-color: #eee;">
      <div class="container py-5 h-100">
        <form action="/loginflask29" method ="post" >
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col col-md-100 col-lg-38  col-xl-38">
            <div class="card" style="border-radius: 15px;">
              <div class="card-body p-2">
                <div class="d-flex text-black">
                  <div class="flex-shrink-0">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-1.webp"
                      alt="Generic placeholder image" class="img-fluid"
                      style="width: 180px; border-radius: 10px;">
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h5 class="mb-1">Danny McLoan</h5>
                    <p class="mb-2 pb-1" style="color: #2b2a2a;">Senior Journalist</p>
                    <div class="d-flex justify-content-start rounded-3 p-2 mb-2"
                      style="background-color: #efefef;">
                      <div>
                        <p class="small text-muted mb-1">number of projects</p>
                        <p class="mb-0">10</p>
                      </div>
                      <div class="px-3">
                        <p class="small text-muted mb-1">average monthly hours</p>
                        <p class="mb-0">240</p>
                      </div>
                      <div>
                        <p class="small text-muted mb-1">time spent in company</p>
                        <p class="mb-0">8</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">work accident</p>
                        <p class="mb-0">4</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">promotion last 5years</p>
                        <p class="mb-0">2</p>
                      </div>
                                                          <div>
                        <p class="small text-muted mb-1">salary range</p>
                        <p class="mb-0">high</p>
                      </div>
                                                          <div>
                        <p class="small text-muted mb-1"> department</p>
                        <p class="mb-0">IT</p>
                      </div>

                                        <div>
                        <p class="small text-muted mb-1">satisfaction this year</p>
                        <p class="mb-0">0.3</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">satisfaction last year</p>
                        <p class="mb-0">0.9</p>
                      </div>
                    </div>
                    <div class="d-flex pt-1">

                      <button type="submit" href="/" class="btn btn-primary flex-grow-1">predict</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        </form>
      </div>
    </section>
    <section class="vh-100" style="background-color: #9de2ff;">
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <section style="background-color: #eee;">
      <div class="container py-5 h-100">
        <form action="/loginflask12" method ="post" >
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col col-md-100 col-lg-38  col-xl-38">
            <div class="card" style="border-radius: 15px;">
              <div class="card-body p-2">
                <div class="d-flex text-black">
                  <div class="flex-shrink-0">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-1.webp"
                      alt="Generic placeholder image" class="img-fluid"
                      style="width: 180px; border-radius: 10px;">
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h5 class="mb-1">Danny McLoan</h5>
                    <p class="mb-2 pb-1" style="color: #2b2a2a;">Senior Journalist</p>
                    <div class="d-flex justify-content-start rounded-3 p-2 mb-2"
                      style="background-color: #efefef;">
                      <div>
                        <p class="small text-muted mb-1">number of projects</p>
                        <p class="mb-0">10</p>
                      </div>
                      <div class="px-3">
                        <p class="small text-muted mb-1">average monthly hours</p>
                        <p class="mb-0">290</p>
                      </div>
                      <div>
                        <p class="small text-muted mb-1">time spent in company</p>
                        <p class="mb-0">9</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">work accident</p>
                        <p class="mb-0">0</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">promotion last 5years</p>
                        <p class="mb-0">3</p>
                      </div>
                                                          <div>
                        <p class="small text-muted mb-1">salary range</p>
                        <p class="mb-0">MEDIUM</p>
                      </div>
                                                          <div>
                        <p class="small text-muted mb-1"> department</p>
                        <p class="mb-0">SERVICE</p>
                      </div>

                                        <div>
                        <p class="small text-muted mb-1">satisfaction this year</p>
                        <p class="mb-0">0.5</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">satisfaction last year</p>
                        <p class="mb-0">0.2</p>
                      </div>
                    </div>
                    <div class="d-flex pt-1">

                      <button type="submit" href="/" class="btn btn-primary flex-grow-1">predict</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        </form>
      </div>
    </section>'''
    a=[[10,290,9,0,3,2,8,0.5,0.2]]
    watagory=['Employee will stay','Employee will Leave']
    pred_result =loaded_model.predict(a)
    u=(int(pred_result))
    w="prediction "+watagory[u]
    return render_template("login.html", q=q,w=w)


@app.route('/loginflask29', methods=['POST', 'GET'])
def loginflask29():
    q = '''<section class="vh-100" style="background-color: #9de2ff;">
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <section style="background-color: #eee;">
      <div class="container py-5 h-100">
        <form action="/loginflask29" method ="post" >
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col col-md-100 col-lg-38  col-xl-38">
            <div class="card" style="border-radius: 15px;">
              <div class="card-body p-2">
                <div class="d-flex text-black">
                  <div class="flex-shrink-0">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-1.webp"
                      alt="Generic placeholder image" class="img-fluid"
                      style="width: 180px; border-radius: 10px;">
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h5 class="mb-1">Danny McLoan</h5>
                    <p class="mb-2 pb-1" style="color: #2b2a2a;">Senior Journalist</p>
                    <div class="d-flex justify-content-start rounded-3 p-2 mb-2"
                      style="background-color: #efefef;">
                      <div>
                        <p class="small text-muted mb-1">number of projects</p>
                        <p class="mb-0">10</p>
                      </div>
                      <div class="px-3">
                        <p class="small text-muted mb-1">average monthly hours</p>
                        <p class="mb-0">240</p>
                      </div>
                      <div>
                        <p class="small text-muted mb-1">time spent in company</p>
                        <p class="mb-0">8</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">work accident</p>
                        <p class="mb-0">4</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">promotion last 5years</p>
                        <p class="mb-0">2</p>
                      </div>
                                                          <div>
                        <p class="small text-muted mb-1">salary range</p>
                        <p class="mb-0">high</p>
                      </div>
                                                          <div>
                        <p class="small text-muted mb-1"> department</p>
                        <p class="mb-0">IT</p>
                      </div>

                                        <div>
                        <p class="small text-muted mb-1">satisfaction this year</p>
                        <p class="mb-0">0.3</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">satisfaction last year</p>
                        <p class="mb-0">0.9</p>
                      </div>
                    </div>
                    <div class="d-flex pt-1">

                      <button type="submit" href="/" class="btn btn-primary flex-grow-1">predict</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        </form>
      </div>
    </section>
    <section class="vh-100" style="background-color: #9de2ff;">
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <section style="background-color: #eee;">
      <div class="container py-5 h-100">
        <form action="/loginflask12" method ="post" >
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col col-md-100 col-lg-38  col-xl-38">
            <div class="card" style="border-radius: 15px;">
              <div class="card-body p-2">
                <div class="d-flex text-black">
                  <div class="flex-shrink-0">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-1.webp"
                      alt="Generic placeholder image" class="img-fluid"
                      style="width: 180px; border-radius: 10px;">
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h5 class="mb-1">Danny McLoan</h5>
                    <p class="mb-2 pb-1" style="color: #2b2a2a;">Senior Journalist</p>
                    <div class="d-flex justify-content-start rounded-3 p-2 mb-2"
                      style="background-color: #efefef;">
                      <div>
                        <p class="small text-muted mb-1">number of projects</p>
                        <p class="mb-0">10</p>
                      </div>
                      <div class="px-3">
                        <p class="small text-muted mb-1">average monthly hours</p>
                        <p class="mb-0">290</p>
                      </div>
                      <div>
                        <p class="small text-muted mb-1">time spent in company</p>
                        <p class="mb-0">9</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">work accident</p>
                        <p class="mb-0">0</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">promotion last 5years</p>
                        <p class="mb-0">3</p>
                      </div>
                                                          <div>
                        <p class="small text-muted mb-1">salary range</p>
                        <p class="mb-0">MEDIUM</p>
                      </div>
                                                          <div>
                        <p class="small text-muted mb-1"> department</p>
                        <p class="mb-0">SERVICE</p>
                      </div>

                                        <div>
                        <p class="small text-muted mb-1">satisfaction this year</p>
                        <p class="mb-0">0.5</p>
                      </div>
                                        <div>
                        <p class="small text-muted mb-1">satisfaction last year</p>
                        <p class="mb-0">0.2</p>
                      </div>
                    </div>
                    <div class="d-flex pt-1">

                      <button type="submit" href="/" class="btn btn-primary flex-grow-1">predict</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        </form>
      </div>
    </section>'''
    a=[[10,240,8,4,2,0,0,0.3,0.9]]
    watagory=['Employee will stay','Employee will Leave']
    pred_result =loaded_model.predict(a)
    u=(int(pred_result))
    w=watagory[u]
    return render_template("login.html", q=q,w=w)

    
@app.route('/loginflask2',methods=['POST','GET'])

def loginflask2():
    q='''<section class="vh-100" style="background-color: #9de2ff;">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<section style="background-color: #eee;">
  <div class="container py-5 h-100">
    <form action="/loginflask29" method ="post" >
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col col-md-100 col-lg-38  col-xl-38">
        <div class="card" style="border-radius: 15px;">
          <div class="card-body p-2">
            <div class="d-flex text-black">
              <div class="flex-shrink-0">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-1.webp"
                  alt="Generic placeholder image" class="img-fluid"
                  style="width: 180px; border-radius: 10px;">
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="mb-1">Danny McLoan</h5>
                <p class="mb-2 pb-1" style="color: #2b2a2a;">Senior Journalist</p>
                <div class="d-flex justify-content-start rounded-3 p-2 mb-2"
                  style="background-color: #efefef;">
                  <div>
                    <p class="small text-muted mb-1">number of projects</p>
                    <p class="mb-0">10</p>
                  </div>
                  <div class="px-3">
                    <p class="small text-muted mb-1">average monthly hours</p>
                    <p class="mb-0">240</p>
                  </div>
                  <div>
                    <p class="small text-muted mb-1">time spent in company</p>
                    <p class="mb-0">8</p>
                  </div>
                                    <div>
                    <p class="small text-muted mb-1">work accident</p>
                    <p class="mb-0">4</p>
                  </div>
                                    <div>
                    <p class="small text-muted mb-1">promotion last 5years</p>
                    <p class="mb-0">2</p>
                  </div>
                                                      <div>
                    <p class="small text-muted mb-1">salary range</p>
                    <p class="mb-0">high</p>
                  </div>
                                                      <div>
                    <p class="small text-muted mb-1"> department</p>
                    <p class="mb-0">IT</p>
                  </div>
                  
                                    <div>
                    <p class="small text-muted mb-1">satisfaction this year</p>
                    <p class="mb-0">0.3</p>
                  </div>
                                    <div>
                    <p class="small text-muted mb-1">satisfaction last year</p>
                    <p class="mb-0">0.9</p>
                  </div>
                </div>
                <div class="d-flex pt-1">

                  <button type="submit" href="/" class="btn btn-primary flex-grow-1">predict</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </form>
  </div>
</section>
<section class="vh-100" style="background-color: #9de2ff;">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<section style="background-color: #eee;">
  <div class="container py-5 h-100">
    <form action="/loginflask12" method ="post" >
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col col-md-100 col-lg-38  col-xl-38">
        <div class="card" style="border-radius: 15px;">
          <div class="card-body p-2">
            <div class="d-flex text-black">
              <div class="flex-shrink-0">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-1.webp"
                  alt="Generic placeholder image" class="img-fluid"
                  style="width: 180px; border-radius: 10px;">
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="mb-1">Danny McLoan</h5>
                <p class="mb-2 pb-1" style="color: #2b2a2a;">Senior Journalist</p>
                <div class="d-flex justify-content-start rounded-3 p-2 mb-2"
                  style="background-color: #efefef;">
                  <div>
                    <p class="small text-muted mb-1">number of projects</p>
                    <p class="mb-0">10</p>
                  </div>
                  <div class="px-3">
                    <p class="small text-muted mb-1">average monthly hours</p>
                    <p class="mb-0">290</p>
                  </div>
                  <div>
                    <p class="small text-muted mb-1">time spent in company</p>
                    <p class="mb-0">9</p>
                  </div>
                                    <div>
                    <p class="small text-muted mb-1">work accident</p>
                    <p class="mb-0">0</p>
                  </div>
                                    <div>
                    <p class="small text-muted mb-1">promotion last 5years</p>
                    <p class="mb-0">3</p>
                  </div>
                                                      <div>
                    <p class="small text-muted mb-1">salary range</p>
                    <p class="mb-0">MEDIUM</p>
                  </div>
                                                      <div>
                    <p class="small text-muted mb-1"> department</p>
                    <p class="mb-0">SERVICE</p>
                  </div>
                  
                                    <div>
                    <p class="small text-muted mb-1">satisfaction this year</p>
                    <p class="mb-0">0.5</p>
                  </div>
                                    <div>
                    <p class="small text-muted mb-1">satisfaction last year</p>
                    <p class="mb-0">0.2</p>
                  </div>
                </div>
                <div class="d-flex pt-1">

                  <button type="submit" href="/" class="btn btn-primary flex-grow-1">predict</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </form>
  </div>
</section>'''
    a=[[10,240,8,4,2,0,0,0.3,0.9]]
    watagory=['Employee will stay','Employee will Leave']
    pred_result =loaded_model.predict(a)
    u=(int(pred_result))
    w=watagory[u]
    return render_template("login.html", q=q)
@app.route('/loginflask6',methods=['POST','GET'])
def loginflask6():
    q='''<form action="/loginflask" method ="post" >
    <input class="fname" type="text"  placeholder="Number of Project" name="email">
          <br><br><br><br><input type="text" placeholder="Average Montly Hours" name="email0">
           <br><br><br><br><input type="text"  placeholder="Time Spend in Company" name="email1">
           <br><br><br><br><input type="text"  placeholder="Work Accident" name="email2">
           <br><br><br><br><input type="text"  placeholder="promotion_last_5years" name="email3">


             <br><br><br><br><select  name="email6">
                  <option value="salary">choose salary</option>
    <option value="high">high</option>
    <option value="medium">medium</option>
    <option value="low">low</option></select>

                       <br><br><br><br><select name="email7">
                  <option value="salary">choose department</option>
    <option value="it">it</option>
    <option value="sales">sales</option>
    <option value="support">support</option>
                          <option value="product_mng">product_mng</option>
    <option value="marketing">marketing</option>
    <option value="hr">hr</option>
                          <option value="management">management</option>
    <option value="accounting">accounting</option>
    <option value="technical">technical</option></select>
                     <br><br><br><br><input type="text"  placeholder="satisfaction level" name="email4"><br><br><br><br>
          <input type="text" placeholder="last evaluation" name="email5">


         <br><br><br><br><button type="submit" href="/">Submit</button>
         </form>'''

    return render_template("login.html", q=q)


if __name__ == '__main__':
    app.run(debug=True)
