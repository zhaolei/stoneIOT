// Automatically generated from the message definition "xnode/Num.msg"
package xnode

import (
	"bytes"
	"encoding/binary"

	"github.com/fetchrobotics/rosgo/ros"
)

type _MsgNum struct {
	text   string
	name   string
	md5sum string
}

func (t *_MsgNum) Text() string {
	return t.text
}

func (t *_MsgNum) Name() string {
	return t.name
}

func (t *_MsgNum) MD5Sum() string {
	return t.md5sum
}

func (t *_MsgNum) NewMessage() ros.Message {
	m := new(Num)
	m.Num = 0
	m.Name = ""
	return m
}

var (
	MsgNum = &_MsgNum{
		`int64 num
string name 
`,
		"xnode/Num",
		"2024f0cf2e6302a28d69fe0f7dfcd317",
	}
)

type Num struct {
	Num  int64  `rosmsg:"num:int64"`
	Name string `rosmsg:"name:string"`
}

func (m *Num) GetType() ros.MessageType {
	return MsgNum
}

func (m *Num) Serialize(buf *bytes.Buffer) error {
	var err error
	binary.Write(buf, binary.LittleEndian, m.Num)
	binary.Write(buf, binary.LittleEndian, uint32(len([]byte(m.Name))))
	buf.Write([]byte(m.Name))
	return err
}

func (m *Num) Deserialize(buf *ros.Reader) error {
	var err error = nil
	if err = binary.Read(buf, binary.LittleEndian, &m.Num); err != nil {
		return err
	}
	{
		var size uint32
		if err = binary.Read(buf, binary.LittleEndian, &size); err != nil {
			return err
		}
		data := make([]byte, int(size))
		if err = binary.Read(buf, binary.LittleEndian, data); err != nil {
			return err
		}
		m.Name = string(data)
	}
	return err
}
