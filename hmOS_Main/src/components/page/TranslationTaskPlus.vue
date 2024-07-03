<template>
    <div>
        <div id="loading" style="display: none">
            <div class="loadEffect">
                <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
            </div>
        </div>
        <!--标题栏-->
        <div class="Hometitlebox">
            <img src="../../assets/img/logo2.png" style="width: 50px; height: 50px; margin-right: 25px" />
            <a style="color: #00e4ff">hmOS1.0</a>
            <img src="../../assets/img/logo1.png" style="width: 60px; height: 50px; margin-left: 15px" />
        </div>
        <!--动效显示-->
        <el-row :gutter="18" style="margin: 30px 60px">
            <el-col :span="14" style="width: 700px;">
                <el-card
                    shadow="hover"
                    style="height: 620px; padding: 5px; background-color: rgba(5, 53, 77, 0.7); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <el-row  style="width: 680px; height: 59px" >
                        <el-col span="10">
                            <div class="header-box1">
                                <img src="../../assets/img/taskinput.png" style="width: 45px; height: 45px" />
                                <span class="header-name">Source Code Input</span>
                            </div>
                        </el-col>
                        <el-col span="8">
                            <div class="next-btn" @click="translate_code()">
                            <a class="flowbutton"><span></span><span></span><span></span><span></span>Translate</a>
                            </div>
                        </el-col>
                    </el-row>
                    <div class="divider div-transparent"></div>
                    <el-row :gutter="20" style="margin-left: 15px">
                        <el-col :span="14" style="width: 630px; padding: 0 5px">
                            <el-form
                                ref="form"
                                :model="form"
                                label-width="160px"
                                class="form-item-name"
                                style=" background-color:rgba(3, 26, 37, 0.3);box-shadow: 0px 0px 10px #837979;border-radius:10px; height: 500px"
                            >
                                <el-col :span="20">
                                    <textarea
                                        class="input1"
                                        id="input_source_code"
                                        v-model="source_code"
                                        style="width: 600px; height: 480px"
                                        autocomplete="off"
                                    ></textarea>
                                </el-col>
                            </el-form>
                        </el-col>
                
                    </el-row>
                </el-card>
            </el-col>
            <el-col :span="16" style="width: 700px;">
                <el-card
                    shadow="hover"
                    style="height: 620px; padding: 5px; background-color: rgba(5, 53, 77, 0.7); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1" style="width: 800px;">
                        <img src="../../assets/img/taskview.png" style="width: 45px; height: 45px" />
                        <span class="header-name">Target Code Output</span>
                    </div>
                    <div class="divider div-transparent"></div>
                    <el-row :gutter="20" style="margin-left: 15px; ">
                        <el-col :span="14" style="width: 640px; height: 680px; padding: 0 5px">
                            <el-form
                                ref="form"
                                :model="form"
                                label-width="160px"
                                class="form-item-name"
                                style=" background-color:rgba(3, 26, 37, 0.3);box-shadow: 0px 0px 10px #837979;border-radius:10px; height: 500px"
                            >
                                <el-col :span="20">
                                    <textarea
                                        ref = "target_code"
                                        class="input1"
                                        id="target_code"
                                        v-model="target_code"
                                        style="width: 610px; height: 480px"
                                        autocomplete="off"
                                    ></textarea>
                                </el-col>
                            </el-form>
                        </el-col>
                
                    </el-row>
                    
                    <div class="next-btn" @click="taskmode()">
                        <a class="flowbutton"><span></span><span></span><span></span><span></span>Next</a>
                    </div>
                </el-card>
            </el-col>

            <el-col :span="2" style="width: 330px; ">
                
                <el-card
                    shadow="hover"
                    style="height: 620px; padding: 5px; background-color: rgba(5, 53, 77, 0.7); border: 0"
                    :body-style="{ padding: '0px' }"
                >
                    <div class="header-box1" style="width: 800px;">
                        <img src="../../assets/img/taskview.png" style="width: 45px; height: 45px" />
                        <span class="header-name">Operations</span>
                        
                    </div>
                    <div class="divider div-transparent"></div>
                    
                    <div class="content-container">
    <div class="choose-div" @click="get_selection()">
      <a class="flowbutton"><span></span><span></span><span></span><span></span>Choose</a>
    </div>

    <!-- 其他内容 -->
    <el-row :gutter="20">
                        <el-col :span="14" >
                            
                                <el-col :span="20">
                                    <textarea
                                        class="input1"
                                        id="modified_code"
                                        v-model="modified_code"
                                        autocomplete="off"
                                    ></textarea>
                                </el-col>
                        </el-col>
                
                    </el-row>

    <div class="next-div" @click="confirm_prefix()">
      <a class="flowbutton"><span></span><span></span><span></span><span></span>Confirm</a>
    </div>

    <div>
      <a class="text">
        <br>
        
    
        <br>
      </a>
      
    </div>

    <div class="next-div" @click="read_form_file()">
      <a class="flowbutton_small"><span></span><span></span><span></span><span></span>READ FROM FILE</a>
    </div>

    <div class="next-div" @click="save_to_file()">
      <a class="flowbutton_small"><span></span><span></span><span></span><span></span>SAVE TO FILE</a>
    </div>

    <div>
      <a class="text">
        <br>
        
    
        <br>
      </a>
      
    </div>

    <div class="next-div" @click="next_code()">
      <a class="flowbutton"><span></span><span></span><span></span><span></span>Next Code</a>
    </div>

  </div>
                        
                    
                    
                    
                   
                    
                    

                    
                </el-card>

            </el-col>

        </el-row>
        <div class="copyrigntoutbox" style="position: relative; top: -22px">
            <span class="copyrigntmsg">Copyright © 2021 Northwestern Polytechnical University All Rights Reserved</span>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import '@/assets/css/style.css';
import '@/assets/css/normalize.min.css';
import '@/assets/css/Datacages_Homeindex.css';
import '@/assets/js/jquery.min.js.下载';
import '@/assets/js/jquery.js.下载';
export default {
    name: 'dashboard',
    data: function () {
        return {
            input1: '',
            input2: '',
            input3: '',
            input4: '',
            input5: '',
            target_code: '',
            source_code: '',
            modified_code: '',
            prefix: '',
            count: 0,
            radio: true,
            radio1: true,
            num1: 0,
            num2: 0,
            num3: 0,
            structure: 1,
            backbone: 1,
            extensionModule: 1
        };
    },
    computed: {},

    methods: {
        taskmode() {
            let input = {
                taskName: this.input1,
               
                iteraction_rounds_limit: this.input2,
                description: this.input5,
                resourceIsCustom: [Number(!this.radio), this.num1, this.num2, this.num3],
                modelIsCustom: [Number(!this.radio1), this.structure, this.backbone, this.extensionModule]
            };
            this.$router.push({
                path: `/translationmain/${JSON.stringify(input)}`
            });
        },
        get_selection(){
            const textarea = this.$refs.target_code;
            const start = textarea.selectionStart;
            const end = textarea.selectionEnd;
            const selectedText = this.target_code.substring(start, end);
            this.modified_code = selectedText
        },
        confirm_prefix(){
            const textarea = this.$refs.target_code;
            const start = textarea.selectionStart;
            this.prefix = this.target_code.substring(0, start) + this.modified_code
            axios.get('http://127.0.0.1:5000/test1?source_code='+this.source_code+'&prefix='+this.prefix+'&id='+this.count)
            .then(response => {
            // 处理返回的数据
            this.target_code = response.data['result']
            console.log(response.data['result']);
            })
            .catch(error => {
            console.error(error);
            });
        },

        read_form_file(){
            const input = document.createElement('input');
            input.type = 'file';
            input.onchange = (e) => {
                const file = e.target.files[0];
                const reader = new FileReader();
                reader.onload = (e) => {
                const content = e.target.result;
                // 将文件内容加载到文本框中
                document.getElementById('input_source_code').value = content;
                };
                reader.readAsText(file);
            };
            input.click();
        },

        save_to_file(){
            const content = document.getElementById('target_code').value;
            const blob = new Blob([content], { type: 'text/plain' });
            const reader = new FileReader();
            reader.onload = function(event) {
            const link = document.createElement('a');
            link.href = event.target.result;
            link.download = 'saved_file.txt';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
  };
  reader.readAsDataURL(blob);
        },

        next_code(){
            this.prefix = ''
            this.count += 1
            this.source_code = ''
            this.target_code = ''
            this.modified_code = ''
        },
        
        translate_code() { 
            
            axios.get('http://127.0.0.1:5000/test1?source_code='+this.source_code+'&prefix='+this.prefix+'&id='+this.count)
            .then(response => {
            // 处理返回的数据
            this.target_code = response.data['result']
            console.log(response.data['result']);
            })
            .catch(error => {
            // 处理错误
            console.error(error);
            });
        }
    },
    mounted() {
        console.clear();
        var MAX_LIFE = 50;
        var canvas = document.querySelector('canvas');
        var input1 = document.getElementById('input1');
        var input2 = document.getElementById('input2');
        var input3 = document.getElementById('input3');
        var input4 = document.getElementById('input4');
        var field = {};
        var hasFocus = false;
        var caret = document.createElement('span');
        caret.style.cssText = document.defaultView.getComputedStyle(document.getElementById('input2'), '').cssText;
        caret.style.position = 'absolute';
        caret.style.left = 0;
        caret.style.top = 0;
        caret.style.width = 'auto';
        caret.style.visibility = 'hidden';
        document.body.appendChild(caret);

        function reposition() {
            field = input1.getBoundingClientRect();
        }
        window.onload = reposition;
        window.onresize = reposition;
        reposition();

        input1.onfocus = function () {
            hasFocus = true;
        };
        input1.onblur = function () {
            hasFocus = false;
        };
        input2.onfocus = function () {
            hasFocus = true;
        };
        input2.onblur = function () {
            hasFocus = false;
        };
        input3.onfocus = function () {
            hasFocus = true;
        };
        input3.onblur = function () {
            hasFocus = false;
        };
        input4.onfocus = function () {
            hasFocus = true;
        };
        input4.onblur = function () {
            hasFocus = false;
        };
        function rain() {}

        function burst(intensity) {
            var behavior = [window.behavior.cohesion(), window.behavior.move()];

            var size = 0.75;
            ``;
            var force = 0.7;
            var lifeMin = 0;
            var progress = Math.min(field.width, caret.offsetWidth) / field.width;
            var offset = field.left + field.width * progress;
            var rangeMin = Math.max(field.left, offset - 30);
            var rangeMax = Math.min(field.right, offset + 10);

            window.spray(intensity, function () {
                return [
                    null,
                    null,
                    Vector.create(Random.between(rangeMin + 10, rangeMax - 20), Random.between(field.top + 15, field.bottom - 15)),
                    Vector.random(force),
                    size + Math.random(),
                    Random.between(lifeMin, 0),
                    behavior
                ];
            });

            // top edge
            window.spray(intensity * 0.5, function () {
                return [
                    null,
                    null,
                    Vector.create(Random.between(rangeMin, rangeMax), field.top),
                    Vector.random(force),
                    size + Math.random(),
                    Random.between(lifeMin, 0),
                    behavior
                ];
            });

            // bottom edge
            window.spray(intensity * 0.5, function () {
                return [
                    null,
                    null,
                    Vector.create(Random.between(rangeMin, rangeMax), field.top + field.height),
                    Vector.random(force),
                    size + Math.random(),
                    Random.between(lifeMin, 0),
                    behavior
                ];
            });

            // left edge
            if (input1.value.length === 1) {
                window.spray(intensity * 2, function () {
                    return [
                        null,
                        null,
                        Vector.create(field.left, Random.between(field.top, field.bottom)),
                        Vector.random(force),
                        size + Math.random(),
                        Random.between(lifeMin, 0),
                        behavior
                    ];
                });
            }
            if (input2.value.length === 1) {
                window.spray(intensity * 2, function () {
                    return [
                        null,
                        null,
                        Vector.create(field.left, Random.between(field.top, field.bottom)),
                        Vector.random(force),
                        size + Math.random(),
                        Random.between(lifeMin, 0),
                        behavior
                    ];
                });
            }
            if (input3.value.length === 1) {
                window.spray(intensity * 2, function () {
                    return [
                        null,
                        null,
                        Vector.create(field.left, Random.between(field.top, field.bottom)),
                        Vector.random(force),
                        size + Math.random(),
                        Random.between(lifeMin, 0),
                        behavior
                    ];
                });
            }
            if (input4.value.length === 1) {
                window.spray(intensity * 2, function () {
                    return [
                        null,
                        null,
                        Vector.create(field.left, Random.between(field.top, field.bottom)),
                        Vector.random(force),
                        size + Math.random(),
                        Random.between(lifeMin, 0),
                        behavior
                    ];
                });
            }

            // right edge
            if (rangeMax == field.right) {
                window.spray(intensity * 2, function () {
                    return [
                        null,
                        null,
                        Vector.create(field.right, Random.between(field.top, field.bottom)),
                        Vector.random(force),
                        size + Math.random(),
                        Random.between(lifeMin, 0),
                        behavior
                    ];
                });
            }
        }

        // start particle simulation
        simulate('2d', {
            init: function () {},
            tick: function (particles) {
                if (!particles) {
                    return;
                }

                particles.forEach(function (p) {
                    if (p.life > MAX_LIFE) {
                        window.destroy(p);
                    }
                });
            },
            beforePaint: function () {
                window.clear();
            },
            paint: function (particle) {
                var p = particle.position;
                var s = particle.size;
                var o = 1 - particle.life / MAX_LIFE;

                window.paint.circle(p.x, p.y, s, 'rgba(255,255,255,' + o + ')');
                window.paint.circle(p.x, p.y, s + 2, 'rgba(231,244,255,' + o * 0.25 + ')');
            },
            afterPaint: function () {
                // nothing
            },
            action1: function (x, y) {
                caret.textContent = input1.value;

                burst.call(this, 10);
                input1.classList.add('keyup');

                setTimeout(function () {
                    input1.classList.remove('keyup');
                }, 100);
            },
            action2: function (x, y) {
                caret.textContent = input1.value;

                burst.call(this, 10);
                input2.classList.add('keyup');

                setTimeout(function () {
                    input2.classList.remove('keyup');
                }, 100);
            },
            action3: function (x, y) {
                caret.textContent = input1.value;

                burst.call(this, 10);
                input3.classList.add('keyup');

                setTimeout(function () {
                    input3.classList.remove('keyup');
                }, 100);
            },
            action4: function (x, y) {
                caret.textContent = input1.value;

                burst.call(this, 10);
                input4.classList.add('keyup');

                setTimeout(function () {
                    input4.classList.remove('keyup');
                }, 100);
            }
        });

        // "simulate" particle simulation logic
        /**
         * Constants
         */
        var PI_2 = Math.PI / 2;
        var PI_180 = Math.PI / 180;

        /**
         * Random
         */
        var Random = {
            between: function (min, max) {
                return min + Math.random() * (max - min);
            }
        };

        /**
         * 2D Vector Class
         */
        function Vector(x, y) {
            this._x = x || 0;
            this._y = y || 0;
        }

        Vector.create = function (x, y) {
            return new Vector(x, y);
        };

        Vector.add = function (a, b) {
            return new Vector(a.x + b.x, a.y + b.y);
        };

        Vector.subtract = function (a, b) {
            return new Vector(a.x - b.x, a.y - b.y);
        };

        Vector.random = function (range) {
            var v = new Vector();
            v.randomize(range);
            return v;
        };

        Vector.distanceSquared = function (a, b) {
            var dx = a.x - b.x;
            var dy = a.y - b.y;
            return dx * dx + dy * dy;
        };

        Vector.distance = function (a, b) {
            var dx = a.x - b.x;
            var dy = a.y - b.y;
            return Math.sqrt(dx * dx + dy * dy);
        };

        Vector.prototype = {
            get x() {
                return this._x;
            },
            get y() {
                return this._y;
            },
            set x(value) {
                this._x = value;
            },
            set y(value) {
                this._y = value;
            },
            get magnitudeSquared() {
                return this._x * this._x + this._y * this._y;
            },
            get magnitude() {
                return Math.sqrt(this.magnitudeSquared);
            },
            get angle() {
                return (Math.atan2(this._y, this._x) * 180) / Math.PI;
            },
            clone: function () {
                return new Vector(this._x, this._y);
            },
            add: function (v) {
                this._x += v.x;
                this._y += v.y;
            },
            subtract: function (v) {
                this._x -= v.x;
                this._y -= v.y;
            },
            multiply: function (value) {
                this._x *= value;
                this._y *= value;
            },
            divide: function (value) {
                this._x /= value;
                this._y /= value;
            },
            normalize: function () {
                var magnitude = this.magnitude;
                if (magnitude > 0) {
                    this.divide(magnitude);
                }
            },
            limit: function (treshold) {
                if (this.magnitude > treshold) {
                    this.normalize();
                    this.multiply(treshold);
                }
            },
            randomize: function (amount) {
                amount = amount || 1;
                this._x = amount * 2 * (-0.5 + Math.random());
                this._y = amount * 2 * (-0.5 + Math.random());
            },
            rotate: function (degrees) {
                var magnitude = this.magnitude;
                var angle = (Math.atan2(this._x, this._y) * PI_HALF + degrees) * PI_180;
                this._x = magnitude * Math.cos(angle);
                this._y = magnitude * Math.sin(angle);
            },
            flip: function () {
                var temp = this._y;
                this._y = this._x;
                this._x = temp;
            },
            invert: function () {
                this._x = -this._x;
                this._y = -this._y;
            },
            toString: function () {
                return this._x + ', ' + this._y;
            }
        };

        /**
         * Particle Class
         */
        function Particle(id, group, position, velocity, size, life, behavior) {
            this._id = id || 'default';
            this._group = group || 'default';

            this._position = position || new Vector();
            this._velocity = velocity || new Vector();
            this._size = size || 1;
            this._life = Math.round(life || 0);

            this._behavior = behavior || [];
        }

        Particle.prototype = {
            get id() {
                return this._id;
            },
            get group() {
                return this._group;
            },
            get life() {
                return this._life;
            },
            get size() {
                return this._size;
            },
            set size(size) {
                this._size = size;
            },
            get position() {
                return this._position;
            },
            get velocity() {
                return this._velocity;
            },
            update: function (stage) {
                this._life++;

                var i = 0;
                var l = this._behavior.length;

                for (; i < l; i++) {
                    this._behavior[i].call(stage, this);
                }
            },
            toString: function () {
                return 'Particle(' + this._id + ') ' + this._life + ' pos: ' + this._position + ' vec: ' + this._velocity;
            }
        };

        // setup DOM
        function simulate(dimensions, options) {
            // private vars
            var particles = [];
            var destroyed = [];
            var update = update || function () {};
            var stage = stage || function () {};
            var canvas;
            var context;

            if (!options) {
                console.error('"options" object must be defined');
                return;
            }

            if (!options.init) {
                console.error('"init" function must be defined');
                return;
            }

            if (!options.paint) {
                console.error('"paint" function must be defined');
                return;
            }

            if (!options.tick) {
                options.tick = function () {};
            }

            if (!options.beforePaint) {
                options.beforePaint = function () {};
            }

            if (!options.afterPaint) {
                options.afterPaint = function () {};
            }

            if (!options.action) {
                options.action = function () {};
            }

            if (document.readyState === 'interactive') {
                setup();
            } else {
                document.addEventListener('DOMContentLoaded', setup);
            }

            // resizes canvas to fit window dimensions
            function fitCanvas() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }

            // create canvas for drawing
            function setup() {
                // create
                canvas = document.createElement('canvas');
                document.body.appendChild(canvas);

                // correct canvas size on window resize
                window.addEventListener('resize', fitCanvas);

                // go
                go();
            }

            // canvas has been attached, let's go!
            function go() {
                // set initial canvas size
                fitCanvas();

                // get context for drawing
                context = canvas.getContext(dimensions);

                // simulation update loop
                function act() {
                    // update particle states
                    var i = 0;
                    var l = particles.length;
                    var p;
                    for (; i < l; i++) {
                        particles[i].update(this);
                    }

                    // clean destroyed particles
                    while ((p = destroyed.pop())) {
                        do {
                            // has not been found in destroyed array?
                            if (p !== particles[i]) {
                                continue;
                            }

                            // remove particle
                            particles.splice(i, 1);
                        } while (i-- >= 0);
                    }

                    // repaint context
                    options.beforePaint.call(this);

                    // repaint particles
                    i = 0;
                    l = particles.length;
                    for (; i < l; i++) {
                        options.paint.call(this, particles[i]);
                    }

                    // after particles have been painted
                    options.afterPaint.call(this);
                }

                function tick() {
                    // call update method, this allows for inserting particles later on
                    options.tick.call(this, particles);

                    // update particles here
                    act();

                    // on to the next frame
                    window.requestAnimationFrame(tick);
                }

                /**
                 * API
                 **/
                function clear() {
                    context.clearRect(0, 0, canvas.width, canvas.height);
                }

                function destroy(particle) {
                    destroyed.push(particle);
                }

                function add(id, group, position, velocity, size, life, behavior) {
                    particles.push(new Particle(id, group, position, velocity, size, life, behavior));
                }

                function spray(amount, config) {
                    var i = 0;
                    for (; i < amount; i++) {
                        add.apply(this, config());
                    }
                }

                function debug(particle) {
                    this.paint.circle(particle.position.x, particle.position.y, particle.size, '#03e9f4');
                    context.beginPath();
                    context.moveTo(particle.position.x, particle.position.y);
                    context.lineTo(particle.position.x + particle.velocity.x * 10, particle.position.y + particle.velocity.y * 10);
                    context.strokeStyle = '#03e9f4';
                    context.stroke();
                    context.closePath();
                }

                window.clear = clear;
                window.destroy = destroy;
                window.add = add;
                window.spray = spray;
                window.debug = debug;

                window.paint = {
                    circle: function (x, y, size, color) {
                        context.beginPath();
                        context.arc(x, y, size, 0, 2 * Math.PI, false);
                        context.fillStyle = color;
                        context.fill();
                    },
                    square: function (x, y, size, color) {
                        context.beginPath();
                        context.rect(x - size * 0.5, y - size * 0.5, size, size);
                        context.fillStyle = color;
                        context.fill();
                    }
                };

                window.behavior = {
                    cohesion: function (range, speed) {
                        range = Math.pow(range || 100, 2);
                        speed = speed || 0.001;
                        return function (particle) {
                            var center = new Vector();
                            var i = 0;
                            var l = particles.length;
                            var count = 0;

                            if (l <= 1) {
                                return;
                            }

                            for (; i < l; i++) {
                                // don't use self in group
                                if (particles[i] === particle || Vector.distanceSquared(particles[i].position, particle.position) > range) {
                                    continue;
                                }

                                center.add(Vector.subtract(particles[i].position, particle.position));
                                count++;
                            }

                            if (count > 0) {
                                center.divide(count);

                                center.normalize();
                                center.multiply(particle.velocity.magnitude);

                                center.multiply(0.05);
                            }

                            particle.velocity.add(center);
                        };
                    },
                    separation: function (distance) {
                        var distance = Math.pow(distance || 25, 2);

                        return function (particle) {
                            var heading = new Vector();
                            var i = 0;
                            var l = particles.length;
                            var count = 0;
                            var diff;

                            if (l <= 1) {
                                return;
                            }

                            for (; i < l; i++) {
                                // don't use self in group
                                if (
                                    particles[i] === particle ||
                                    Vector.distanceSquared(particles[i].position, particle.position) > distance
                                ) {
                                    continue;
                                }

                                // stay away from neighbours
                                diff = Vector.subtract(particle.position, particles[i].position);
                                diff.normalize();

                                heading.add(diff);
                                count++;
                            }

                            if (count > 0) {
                                // get average
                                heading.divide(count);

                                // make same length as current velocity (so particle won't speed up)
                                heading.normalize();
                                heading.multiply(particle.velocity.magnitude);

                                // limit force to make particle movement smoother
                                heading.limit(0.1);
                            }

                            particle.velocity.add(heading);
                        };
                    },
                    alignment: function (range) {
                        range = Math.pow(range || 100, 2);
                        return function (particle) {
                            var i = 0;
                            var l = particles.length;
                            var count = 0;
                            var heading = new Vector();

                            if (l <= 1) {
                                return;
                            }

                            for (; i < l; i++) {
                                // don't use self in group also don't align when out of range
                                if (particles[i] === particle || Vector.distanceSquared(particles[i].position, particle.position) > range) {
                                    continue;
                                }

                                heading.add(particles[i].velocity);
                                count++;
                            }

                            if (count > 0) {
                                heading.divide(count);
                                heading.normalize();
                                heading.multiply(particle.velocity.magnitude);

                                // limit
                                heading.multiply(0.1);
                            }

                            particle.velocity.add(heading);
                        };
                    },
                    move: function () {
                        return function (particle) {
                            particle.position.add(particle.velocity);

                            // handle collisions?
                        };
                    },
                    eat: function (food) {
                        food = food || [];
                        return function (particle) {
                            var i = 0;
                            var l = particles.length;
                            var prey;

                            for (; i < l; i++) {
                                prey = particles[i];

                                // can't eat itself, also, needs to be tasty
                                if (prey === particle || food.indexOf(prey.group) === -1) {
                                    continue;
                                }

                                // calculate force vector
                                if (Vector.distanceSquared(particle.position, neighbour.position) < 2 && particle.size >= neighbour.size) {
                                    particle.size += neighbour.size;
                                    destroy(neighbour);
                                }
                            }
                        };
                    },
                    force: function (x, y) {
                        return function (particle) {
                            particle.velocity.x += x;
                            particle.velocity.y += y;
                        };
                    },
                    limit: function (treshold) {
                        return function (particle) {
                            particle.velocity.limit(treshold);
                        };
                    },
                    attract: function (forceMultiplier, groups) {
                        forceMultiplier = forceMultiplier || 1;
                        groups = groups || [];
                        return function (particle) {
                            // attract other particles
                            var totalForce = new Vector(0, 0);
                            var force = new Vector(0, 0);
                            var i = 0;
                            var l = particles.length;
                            var distance;
                            var pull;
                            var attractor;
                            var grouping = groups.length;

                            for (; i < l; i++) {
                                attractor = particles[i];

                                // can't be attracted by itself or mismatched groups
                                if (attractor === particle || (grouping && groups.indexOf(attractor.group) === -1)) {
                                    continue;
                                }

                                // calculate force vector
                                force.x = attractor.position.x - particle.position.x;
                                force.y = attractor.position.y - particle.position.y;
                                distance = force.magnitude;
                                force.normalize();

                                // the bigger the attractor the more force
                                force.multiply(attractor.size / distance);

                                totalForce.add(force);
                            }

                            totalForce.multiply(forceMultiplier);

                            particle.velocity.add(totalForce);
                        };
                    },
                    wrap: function (margin) {
                        return function (particle) {
                            // move around when particle reaches edge of screen
                            var position = particle.position;
                            var radius = particle.size * 0.5;

                            if (position.x + radius > canvas.width + margin) {
                                position.x = radius;
                            }

                            if (position.y + radius > canvas.height + margin) {
                                position.y = radius;
                            }

                            if (position.x - radius < -margin) {
                                position.x = canvas.width - radius;
                            }

                            if (position.y - radius < -margin) {
                                position.y = canvas.height - radius;
                            }
                        };
                    },
                    reflect: function () {
                        return function (particle) {
                            // bounce from edges
                            var position = particle.position;
                            var velocity = particle.velocity;
                            var radius = particle.size * 0.5;

                            if (position.x + radius > canvas.width) {
                                velocity.x = -velocity.x;
                            }

                            if (position.y + radius > canvas.height) {
                                velocity.y = -velocity.y;
                            }

                            if (position.x - radius < 0) {
                                velocity.x = -velocity.x;
                            }

                            if (position.y - radius < 0) {
                                velocity.y = -velocity.y;
                            }
                        };
                    },
                    edge: function (action) {
                        return function (particle) {
                            var position = particle.position;
                            var velocity = particle.velocity;
                            var radius = particle.size * 0.5;

                            if (position.x + radius > canvas.width) {
                                action(particle);
                            }

                            if (position.y + radius > canvas.height) {
                                action(particle);
                            }

                            if (position.x - radius < 0) {
                                action(particle);
                            }

                            if (position.y - radius < 0) {
                                action(particle);
                            }
                        };
                    }
                };

                // public
                Object.defineProperties(window, {
                    particles: {
                        get: function () {
                            return particles;
                        }
                    },
                    width: {
                        get: function () {
                            return canvas.width;
                        }
                    },
                    height: {
                        get: function () {
                            return canvas.height;
                        }
                    },
                    context: {
                        get: function () {
                            return context;
                        }
                    }
                });

                // call init method so the scene can be setup
                options.init.call(this);

                // start ticking
                tick();

                // start listening to events
                var self = this;
                document.getElementById('input1').addEventListener('keyup', function (e) {
                    options.action1.call(self, e.pageX, e.pageY);
                });
                document.getElementById('input2').addEventListener('keyup', function (e) {
                    options.action2.call(self, e.pageX, e.pageY);
                });
                document.getElementById('input3').addEventListener('keyup', function (e) {
                    options.action3.call(self, e.pageX, e.pageY);
                });
                document.getElementById('input4').addEventListener('keyup', function (e) {
                    options.action4.call(self, e.pageX, e.pageY);
                });
            }
        }
    }
};
</script>

<style scoped>
.loadEffect {
    width: 100px;
    height: 100px;
    position: relative;
    margin: 0 auto;
    top: 26%;
}

.loadEffect span {
    animation: load 1.04s ease infinite;
    display: inline-block;
    width: 30px;
    height: 10px;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
    background: lightgreen;
    position: absolute;
}

.loadEffect span:nth-child(1) {
    left: 0;
    top: 50%;
    margin-top: -5px;
    animation-delay: 0.13s;
}

.loadEffect span:nth-child(2) {
    left: 10px;
    top: 20px;
    transform: rotate(45deg);
    animation-delay: 0.26s;
}

.loadEffect span:nth-child(3) {
    left: 50%;
    top: 10px;
    margin-left: -15px;
    transform: rotate(90deg);
    animation-delay: 0.39s;
}

.loadEffect span:nth-child(4) {
    top: 20px;
    right: 10px;
    transform: rotate(135deg);
    animation-delay: 0.52s;
}

.loadEffect span:nth-child(5) {
    right: 0;
    top: 50%;
    margin-top: -5px;
    transform: rotate(180deg);
    animation-delay: 0.65s;
}

.loadEffect span:nth-child(6) {
    right: 10px;
    bottom: 20px;
    transform: rotate(225deg);
    animation-delay: 0.78s;
}

.loadEffect span:nth-child(7) {
    bottom: 10px;
    left: 50%;
    margin-left: -15px;
    transform: rotate(270deg);
    animation-delay: 0.91s;
}

.loadEffect span:nth-child(8) {
    bottom: 20px;
    left: 10px;
    transform: rotate(315deg);
    animation-delay: 1.04s;
}

@keyframes load {
    0% {
        opacity: 1;
    }

    100% {
        opacity: 0.2;
    }
}
#loading {
    background-color: #181e20;
    opacity: 0.5;
    width: 100%;
    height: 100%;
    position: fixed;
    z-index: 999;
}
.grid-content {
    display: flex;
    align-items: center;
    height: 40px;
}

.grid-cont-right {
    flex: 1;
    text-align: center;
    font-size: 14px;
    color: #999;
}

.grid-num {
    font-size: 24px;
    font-weight: bold;
}

.grid-con-icon {
    font-size: 24px;
    width: 40px;
    height: 40px;
    text-align: center;
    line-height: 40px;
    color: #fff;
}

.grid-con-1 .grid-con-icon {
    background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
    color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
    background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
    color: rgb(45, 140, 240);
}

.grid-con-3 .grid-con-icon {
    background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
    color: rgb(242, 94, 67);
}

.user-info {
    display: flex;
    align-items: center;
    padding-bottom: 20px;
    border-bottom: 2px solid #ccc;
    margin-bottom: 20px;
}

.user-avator {
    width: 120px;
    height: 120px;
    border-radius: 50%;
}

.user-info-cont {
    padding-left: 50px;
    flex: 1;
    font-size: 14px;
    color: #999;
}

.user-info-cont div:first-child {
    font-size: 30px;
    color: #222;
}

.user-info-list {
    font-size: 14px;
    color: #999;
    line-height: 25px;
}

.user-info-list span {
    margin-left: 70px;
}

.mgb20 {
    margin-bottom: 20px;
}

.todo-item {
    font-size: 14px;
}

.todo-item-del {
    text-decoration: line-through;
    color: #999;
}

.schart {
    width: 100%;
    height: 300px;
}
.pre-img {
    width: 100px;
    height: 130px;
    background: #f8f8f8;
    border: 1px solid #eee;
    border-radius: 5px;
    margin-left: 10px;
}
.crop-demo {
    width: 300px;
    border: 2px solid gray;
    border-radius: 15px;
    padding: 5px;
    margin-top: 10px;
    margin-bottom: 10px;
}
.crop-demo-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 20px;
    margin-left: 5px;
    background-color: #409eff;
    color: #fff;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
}
.submit-crop-demo-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 20px;
    margin-left: 5px;
    margin-top: 10px;
    background-color: #409eff;
    color: #fff;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
}
.next-btn {
    position: relative;
    width: 100px;
    height: 40px;
    line-height: 40px;
    padding: 0 25px;
    margin-left: 150px;
    margin-top: 10px;
    font-size: 14px;
    border-radius: 4px;
    box-sizing: border-box;
    cursor: pointer;
}
.crop-input {
    position: absolute;
    width: 20px;
    height: 40px;
    left: 0;
    top: 0;
    opacity: 0;
    cursor: pointer;
}
.upload-demo {
    margin-top: 10px;
}
.query_input {
    margin-left: 360px;
}
.crop-btn-box {
    margin-top: 18px;
    margin-right: 40px;
    float: right;
}
.header-box1 {
    width: 300px;
    height: 50px;
    /* background: url('../../assets/img/icon-typebackground.png') no-repeat; */
    background-size: 100% 100%;
    display: flex;
    align-items: left;
    margin-bottom: 10px;
}
.resource-box {
    display: flex;
    text-align: center;
    margin-left: 50px;
    margin-top: 35px;
}
.resourcenum {
    display: flex;
    flex-direction: column;
    text-align: center;
}
.number-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 60px;
}
.button-box {
    display: flex;
    align-items: center;
    justify-content: center;
}
.net-box {
    display: flex;
    align-items: center;
    padding: 5px;
    background: rgba(114, 160, 184, 0.2);
    margin: 20px 10px 20px 10px;
     background:rgba(3, 26, 37, 0.4);
     box-shadow: 0px 0px 10px #837979;border-radius:10px;
}
.net-name {
    display: flex;
    width: 200px;
    height: 50px;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 800;
    color: #03e9f4;
    text-align: center;
}
.net-select {
    width: 250px;
    height: 100px;
    padding-top: 9px;
    margin-left: 4px;
    display: flex;
    align-items: center;
    
}
.flowbutton {
    position: relative;
    display: inline-block;
    padding: 0px 0px;
    margin: 10px 0;
    color: #03e9f4;
    text-decoration: none;
    text-transform: uppercase;
    transition: 0.5s;
    letter-spacing: 4px;
    font-size: 30px;
    font-weight: 500;
    overflow: hidden;
    margin-right: 50px;
}

.flowbutton_small {
    position: relative;
    display: inline-block;
    padding: 0px 0px;
    margin: 10px 0;
    color: #03e9f4;
    text-decoration: none;
    text-transform: uppercase;
    transition: 0.5s;
    letter-spacing: 4px;
    font-size: 20px;
    font-weight: 500;
    overflow: hidden;
    margin-right: 50px;
}

.flowbutton:hover {
    background: #03e9f4;
    color: #050801;
    box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4, 0 0 200px #03e9f4;
    -webkit-box-reflect: below 1px linear-gradient(transparent, #0005);
}

.flowbutton span {
    position: absolute;
    display: block;
}

.flowbutton span:nth-child(1) {
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, transparent, #03e9f4);
    animation: animate1 1s linear infinite;
}

.flowbutton_small:hover {
    background: #03e9f4;
    color: #050801;
    box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4, 0 0 200px #03e9f4;
    -webkit-box-reflect: below 1px linear-gradient(transparent, #0005);
}

.flowbutton_small span {
    position: absolute;
    display: block;
}

.flowbutton_small span:nth-child(1) {
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, transparent, #03e9f4);
    animation: animate1 1s linear infinite;
}

@keyframes animate1 {
    0% {
        left: -100%;
    }
    50%,
    100% {
        left: 100%;
    }
}

.flowbutton span:nth-child(2) {
    top: -100%;
    right: 0;
    width: 3px;
    height: 100%;
    background: linear-gradient(180deg, transparent, #03e9f4);
    animation: animate2 1s linear infinite;
    animation-delay: 0.25s;
}

@keyframes animate2 {
    0% {
        top: -100%;
    }
    50%,
    100% {
        top: 100%;
    }
}

.flowbutton span:nth-child(3) {
    bottom: 0;
    right: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(270deg, transparent, #03e9f4);
    animation: animate3 1s linear infinite;
    animation-delay: 0.5s;
}

@keyframes animate3 {
    0% {
        right: -100%;
    }
    50%,
    100% {
        right: 100%;
    }
}

.flowbutton span:nth-child(4) {
    bottom: -100%;
    left: 0;
    width: 3px;
    height: 100%;
    background: linear-gradient(360deg, transparent, #03e9f4);
    animation: animate4 1s linear infinite;
    animation-delay: 0.75s;
}

@keyframes animate4 {
    0% {
        bottom: -100%;
    }
    50%,
    100% {
        bottom: 100%;
    }
}
.header-name {
    color: rgb(0, 228, 255);
    margin-left: 20px;
    font-size: 24px;
    font-weight: 1000;
    cursor: pointer;
}
.form-item-name >>> .el-form-item__label {
    color: #03e9f4;
    line-height: 60px;
    font-size: 18px;
    font-weight: 400;
}

.input1 {
    border: 2px solid #03e9f4;
    font-size: 1.5em;
    padding: 0.25em 0.5em 0.3125em;
    color: #03e9f4;
    border-radius: 0.25em;
    /* background: transparent; */
    background: rgba(168, 184, 192, 0.2);
    -webkit-transition: all 0.1s;
    transition: all 0.1s;
    margin: 10px auto;
}

.input1:focus {
    outline: none;
    color: #03e9f4;
    border-color: #03e9f4;
}

.input1.keyup {
    color: white;
    border-color: white;
    text-shadow: 0 0 0.125em white;
    box-shadow: 0 0 0.25em white, inset 0 0 0.25em white;
}

canvas {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    pointer-events: none;
}

.input1 {
    font-family: 'Arial Rounded MT Bold', 'Helvetica Rounded', Arial, sans-serif;
}

::input1-placeholder {
    color: #03e9f4;
    text-shadow: 0 0 0.125em transparent;
    -webkit-transition: all 0.25s;
    transition: all 0.25s;
}

.input1:focus::-webkit-input-placeholder {
    opacity: 0.5;
}

::-moz-placeholder {
    color: #03e9f4;
    text-shadow: 0 0 0.125em transparent;
    -webkit-transition: all 0.25s;
    transition: all 0.25s;
}

.input1:focus::-moz-placeholder {
    opacity: 0.5;
}

:-ms-input1-placeholder {
    color: #03e9f4;
    text-shadow: 0 0 0.125em transparent;
    -webkit-transition: all 0.25s;
    transition: all 0.25s;
}

.input1:focus:-ms-input-placeholder {
    opacity: 0.5;
}
.el-radio >>> .el-radio__inner {
    border-color: #03e9f4;
}
.el-radio >>> .el-radio__label {
    color: #03e9f4;
}
.divider {
    position: relative;
    margin-top: 5px;
    margin-bottom: 15px;
    height: 2px;
}
.div-transparent:before {
    content: '';
    position: absolute;
    top: 0;
    width: 100%;
    height: 1px;
    background-image: linear-gradient(to right, transparent, darkgrey, transparent);
}
</style>