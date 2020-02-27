'''
C# Console app
'''
from shared.runner import TestTraits, Runner

EXENAME = 'crossgen'

if __name__ == "__main__":
    traits = TestTraits(exename=EXENAME,
                        startupmetric='ProcessTime',
                        crossgen=True,
                        guiapp='false',
                        )
    Runner(traits).run()