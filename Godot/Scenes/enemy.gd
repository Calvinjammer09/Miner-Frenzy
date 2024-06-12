extends CharacterBody2D


@onready var anim = get_node('EnemyAnimation')

const SPEED = 300
var health = 9

var damage = 3

func _ready():
	add_to_group('enemies')
	anim.play('move')

func _physics_process(_delta):
	if health <= 0:
		death()
	
	velocity.x = 0
	velocity.y = 0
	
	var x = $'/root/Game/Player'.position.x + (get_viewport_rect().size.x / 2) - position.x
	var y = $'/root/Game/Player'.position.y + (get_viewport_rect().size.y / 2) - position.y

	var hyp = sqrt(x ** 2 + y ** 2)
	
	var cosine = x/hyp
	var sine = y/hyp
	
	velocity.x += cosine * SPEED
	velocity.y += sine * SPEED
	
	if velocity.x <= 0:
		anim.flip_h = true
	else:
		anim.flip_h = false
	
	move_and_slide()

func death():
	queue_free()
