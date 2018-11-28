class Phone(object):

    # NTS: There needs to be a way to ingest the values of a phone into a Phone object neatly.

    def __init__(self,
                 # All keyword arguments are arrays of length 2
                 # Value 0 is the beginning position
                 # Value 1 is the end
                 # This represents phones where the vocal organs move
                 u_lip_y =dict(start=None, end=None),
                 l_lip_y =dict(start=None, end=None),
                 l_puckering =dict(start=None, end=None),
                 l_width =dict(start=None, end=None),
                 l_jaw_x =dict(start=None, end=None),
                 l_jaw_y =dict(start=None, end=None),
                 t_apex_y =dict(start=None, end=None),
                 t_dorsum_y =dict(start=None, end=None),
                 t_foramen_y =dict(start=None, end=None),
                 t_lateral =dict(start=None, end=None),
                 tongue_x =dict(start=None, end=None),
                 vm_closure =dict(start=None, end=None),
                 eg_closure =dict(start=None, end=None),
                 ph_closure =dict(start=None, end=None),
                 v_resonance =dict(start=[None] * 3, end=[None] * 3),
                 ):

        # =Lips=

        # Upper lip distance from resting position up to maximum "snarl" where the teeth are wholly exposed (0-100)
        self.u_lip_y = u_lip_y
        # Lower lip distance from resting position down to where the bottom teeth are wholly exposed (0-100)
        self.l_lip_y = l_lip_y
        # Puckering: how tensed the obicularis oris are measured in normalised contraction (0-100)
        self.l_puckering = l_puckering
        # Width: distance of the corners of the mouth from the centre (0-100).
        # Width must be 0 if puckering is 100
        self.l_width = l_width

        # =Lower jaw=
        # Measured in minimum-to-maximum extension

        # Lower jaw, axis moving towards and away from throat.
        self.l_jaw_x = l_jaw_x
        # Lower jaw, axis moving up and down from upper jaw
        self.l_jaw_y = l_jaw_y

        # =Tongue=
        # Measured from lowest possible position to highest possible position in the mouth (0-100)
        # NTS: Explain what 0 and 100 of each would represent.

        # Tip: apex of tongue. 0 = below bottom teeth, 100 = pressed into roof of mouth
        self.t_apex = t_apex_y
        # Middle: dorsum of tongue. 0 = resting, 100 = pressed into roof of mouth
        self.t_dorsum = t_dorsum_y
        # Back: foramen caecum. 0 = resting, 100 = pressed into roof of mouth
        self.t_foramen_c = t_foramen_y
        # Lateral edges: how rolled into a tube the tongue is
        self.t_lateral = t_lateral
        # Retraction of the tongue: how far forward or back the dorsum is. 100 = past both lips, 0 = under the velum
        self.tongue_x = tongue_x

        # =Throat=

        # Velum: proximity to the pharyngeal wall from fully open to fully closed (0-100)
        self.vm_closure = vm_closure
        # Epiglottis: closure of epiglottis, from fully open to fully closed (0-10)
        self.eg_closure = eg_closure
        # Pharynx: closure of pharyngeal opening by the back of the tongue (0-100)
        self.ph_closure = ph_closure
        # Vocal resonance: the resonance created by the vocal folds.
        # NB pitch is not relevant as the same vowel can be uttered at different pitches
        # Resonance must be represented as a list of 3 values which all represent Hz
        self.v_resonance = v_resonance

        # NTS: How to represent stress?
        # NTS: It shouldn't lie at the Phone level. It should be in the Word level.

        # NTS: There must be a way to represent an irrelevant vocal organ, which does not affect the sound.

        # Calculate air routes and forces based on the values of the above.
        # Also calculate a normalised frequency of the air based on a generic skull and organs
        # You should be able to customise values of the skull and organs to get a specific frequency

        # =Airflow values=
        # These are all calculated as effects based on the values of class attributes.

        # NTS: Any value that = None is a placeholder. These will be mathematical functions of the attributes.

        # Airflow
        self.nasal_airflow_percent = None
        self.oral_airflow_percent = None

        # Air pressure at exits
        self.nasal_airpressure = None
        self.uvular_airpressure = None
        self.velar_airpressure = None
        self.palatal_airpressure = None
        self.alveolar_airpressure = None
        self.dental_airpressure = None
        self.labial_airpressure = None