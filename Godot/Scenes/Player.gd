extends CharacterBody2D


@onready var anim = get_node('PlayerAnimation')

var health = 5
var speed = 500

var can_shoot = true
var can_take_damage = true

signal shoot
signal dead

func get_input():
	var input_dir = Input.get_vector('left', 'right', 'up', 'down')
	var exit = Input.is_action_just_pressed('exit')
	var shot = Input.is_mouse_button_pressed(MOUSE_BUTTON_LEFT)
	velocity = input_dir.normalized() * speed
	
	if exit:
		get_tree().quit()
	
	return shot

func _physics_process(_delta):
	var shot = get_input()
	if velocity:
		anim.play('run')
		if velocity.x:
			if velocity.x > 0:
				anim.flip_h = false
			else:
				anim.flip_h = true
	else:
		anim.play('idle')
		
	if shot and can_shoot:
		var dir = get_global_mouse_position() - position
		shoot.emit(position, dir)
		can_shoot = false
		$ShotTimer.start()
	
	move_and_slide()
	
	if health <= 0:
		dead.emit(true)
		get_tree().change_scene_to_file("res://end.tscn")
	
	var overlap = $PlayerArea.get_overlapping_areas()
	
	if overlap:
		collide_with_enemies()

func _on_shot_timer_timeout():
	can_shoot = true

func collide_with_enemies(damage=0):
	if can_take_damage and health >= 1:
		health -= damage
		can_take_damage = false

func _on_damage_timer_timeout():
	can_take_damage = true
