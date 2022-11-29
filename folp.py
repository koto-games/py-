import fo

fo.create('-0')
fo.record('-0', 'koto', fo.read('-0')['koto']+1)