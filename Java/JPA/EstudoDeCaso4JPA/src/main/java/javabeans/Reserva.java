package javabeans;

import java.io.Serializable;
import java.util.Date;
import java.util.Objects;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
import javax.persistence.Version;

@Entity
public class Reserva implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Id
    @ManyToOne(cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    @JoinColumn(name = "id_passageiro")
    private Passageiro passageiro;
    
    @Id
    @ManyToOne(cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    @JoinColumn(name = "id_voo")
    private Voo voo;
    
    @Column(nullable = false, unique = true)
    private int codigo;
    
    @Temporal(TemporalType.DATE)
    @Column(nullable = false)
    private Date data_reserva;
    
    @Version
    private int versao;

    public Reserva() {
        this.id = 0L;
        this.passageiro = null;
        this.voo = null;
        this.codigo = 0;
        this.data_reserva = new Date();
        this.versao = 0;
    }
    
    public Reserva(Long id, Passageiro passageiro, Voo voo, int codigo, Date data_reserva, int versao) {
        this.id = id;
        this.passageiro = passageiro;
        this.voo = voo;
        this.codigo = codigo;
        this.data_reserva = data_reserva;
        this.versao = versao;
    }
    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Passageiro getPassageiro() {
        return passageiro;
    }

    public void setPassageiro(Passageiro passageiro) {
        this.passageiro = passageiro;
    }

    public Voo getVoo() {
        return voo;
    }

    public void setVoo(Voo voo) {
        this.voo = voo;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public Date getData_reserva() {
        return data_reserva;
    }

    public void setData_reserva(Date data_reserva) {
        this.data_reserva = data_reserva;
    }

    public int getVersao() {
        return versao;
    }

    public void setVersao(int versao) {
        this.versao = versao;
    }

    @Override
    public int hashCode() {
        int hash = 5;
        hash = 59 * hash + Objects.hashCode(this.id);
        hash = 59 * hash + Objects.hashCode(this.passageiro);
        hash = 59 * hash + Objects.hashCode(this.voo);
        hash = 59 * hash + this.codigo;
        hash = 59 * hash + Objects.hashCode(this.data_reserva);
        hash = 59 * hash + this.versao;
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Reserva other = (Reserva) obj;
        if (this.codigo != other.codigo) {
            return false;
        }
        if (this.versao != other.versao) {
            return false;
        }
        if (!Objects.equals(this.id, other.id)) {
            return false;
        }
        if (!Objects.equals(this.passageiro, other.passageiro)) {
            return false;
        }
        if (!Objects.equals(this.voo, other.voo)) {
            return false;
        }
        if (!Objects.equals(this.data_reserva, other.data_reserva)) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return Long.toString(this.id);
    }
    
}
