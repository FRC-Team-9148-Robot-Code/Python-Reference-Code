# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import wpilib
import rev

class Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()

        leftMotor = rev.SparkMax(1, rev.SparkLowLevel.MotorType.kBrushed)
        rightMotor = rev.SparkMax(2, rev.SparkLowLevel.MotorType.kBrushed)
        self.robotDrive = wpilib.DifferentialDrive(leftMotor, rightMotor)
        self.driverController = wpilib.XboxController(0)

    def teleopPeriodic(self):
        self.robotDrive.tankDrive(-self.driverController.getLeftY(), -self.driverController.getRightY())

if __name__ == "__main__":
    wpilib.run(Robot)