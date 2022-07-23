from BalisticMotionCalculator.Src.ballistic_motion import BallisticMotion

if __name__ == '__main__':
    try:
        ballistic = BallisticMotion(initial_angle=45, initial_height=5, initial_velocity=50)
        print(f"Horizontal Distance: {ballistic.calculate_landing_position()}")
        print(f"Final Velocity: {ballistic.calculate_landing_velocity()}")
        print(f"Landing Angle: {ballistic.calculate_landing_angle()}")
    except Exception as e:
        raise e
