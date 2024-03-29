import typing
from commands2 import Command
from wpilib import Preferences
from subsystems.drivesubsystem import DriveSubsystem


class FieldRelativeDrive(Command):
    def __init__(
        self,
        drive: DriveSubsystem,
        forward: typing.Callable[[], float],
        sideways: typing.Callable[[], float],
        rotation: typing.Callable[[], float],
    ) -> None:
        Command.__init__(self)
        self.setName(__class__.__name__)

        self.drive = drive
        self.forward = forward
        self.sideways = sideways
        self.rotation = rotation

        self.addRequirements(self.drive)
        self.setName(__class__.__name__)
        Preferences.initFloat("Robot Relative Sensitivity", 0.4)

    def execute(self) -> None:
        self.drive.arcadeDriveWithFactors(
            self.forward(),
            self.sideways(),
            self.rotation()
            * Preferences.getFloat("Robot Relative Sensitivity"),  # better control
            DriveSubsystem.CoordinateMode.FieldRelative,
        )
