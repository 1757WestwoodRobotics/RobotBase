import typing
from commands2 import Command
from wpilib import Preferences
from subsystems.drivesubsystem import DriveSubsystem


class ArcadeDrive(Command):  # Arcade drive is just robot relative, but no sideways
    def __init__(
        self,
        drive: DriveSubsystem,
        forward: typing.Callable[[], float],
        rotation: typing.Callable[[], float],
    ) -> None:
        Command.__init__(self)
        self.setName(__class__.__name__)

        self.drive = drive
        self.forward = forward
        self.rotation = rotation

        self.addRequirements(self.drive)
        self.setName(__class__.__name__)
        Preferences.initFloat("Robot Relative Sensitivity", 0.2)

    def execute(self) -> None:
        self.drive.arcadeDriveWithFactors(
            self.forward(),
            0,
            self.rotation()
            * Preferences.getFloat("Robot Relative Sensitivity", 0.2),  # better control
            DriveSubsystem.CoordinateMode.RobotRelative,
        )
