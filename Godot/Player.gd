extends CharacterBody2D


const SPEED = 100
const JUMP_VELOCITY = -400.0

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

@onready var anim = get_node('PlayerAnimation')

func _physics_process(delta):
	if Input.is_key_pressed(KEY_W) or Input.is_key_pressed(KEY_S) or Input.is_key_pressed(KEY_D) or Input.is_key_pressed(KEY_A):
		anim.play('run')
		if Input.is_key_pressed(KEY_A):
			position.x -= SPEED * delta
			get_node('PlayerAnimation').flip_h = true
		if Input.is_key_pressed(KEY_D):
			position.x += SPEED * delta
			get_node('PlayerAnimation').flip_h = false
		if Input.is_key_pressed(KEY_S):
			position.y += SPEED * delta
		if Input.is_key_pressed(KEY_W):
			position.y -= SPEED * delta
	else:
		anim.play('idle')
	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	
	move_and_slide()
